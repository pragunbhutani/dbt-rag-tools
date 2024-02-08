import chromadb
import chromadb.utils.embedding_functions as embedding_functions

from dbt_rag_tools.dbt_model import DbtModel


class VectorStore:
    """
    A class representing a vector store for dbt models.

    Methods:
        get_client: Returns the client object for the vector store.
        upsert_models: Upsert the models into the vector store.
        reset_collection: Clear the collection of all documents.
    """

    def __init__(
        self,
        openai_api_key: str,
        embedding_model_name: str = "text-embedding-3-large",
        db_persist_path: str = "./chroma.db",
    ) -> None:
        """
        Initializes a vector store for dbt models.

        Args:
            openai_api_key (str): Your OpenAI API key.
            embedding_model_name (str, optional): The name of the OpenAI embedding model to be used.
            db_persist_path (str, optional): The path to the persistent database file. Defaults to "./chroma.db".
        """
        self.__client = chromadb.PersistentClient(db_persist_path)

        self.__embedding_fn = embedding_functions.OpenAIEmbeddingFunction(
            api_key=openai_api_key, model_name=embedding_model_name
        )

        self.__collection = self.__create_collection__()

        return None

    def __create_collection__(self, distance_fn: str = "l2") -> chromadb.Collection:
        """
        Create a new collection in the vector store.

        Args:
            distance_fn (str, optional): The distance function to be used for nearest neighbour search.
                Defaults to "l2".

        Returns:
            chromadb.Collection: The newly created collection.
        """
        return self.__client.get_or_create_collection(
            name="dbt_models",
            metadata={"hnsw:space": distance_fn},
            embedding_function=self.__embedding_fn,
        )

    def get_client(self) -> chromadb.PersistentClient:
        """
        Returns the client object for the vector store.

        Returns:
            chromadb.PersistentClient: The client object for the vector store.
        """
        return self.__client

    def upsert_models(
        self,
        models: list[DbtModel],
    ) -> None:
        """
        Upsert the models into the vector store.

        Args:
            models (list[DbtModel]): A list of dbt model objects to be upserted into the vector store.

        Returns:
            None
        """
        documents = []
        metadatas = []
        ids = []

        for model in models:
            documents.append(model.as_prompt_text())
            metadatas.append({"file_path": "", "tags": "", "token_length": ""})
            ids.append(model.name)

        return self.__collection.upsert(
            documents=documents, metadatas=metadatas, ids=ids
        )

    def query_collection(self, query: str, n_results: int = 3) -> list[str]:
        """
        Query the collection for the k nearest neighbours to the query.

        Args:
            query (str): The query to be used for nearest neighbour search.
            n_results (int, optional): The number of nearest neighbours to be returned. Defaults to 3.

        Returns:
            list[str]: A list of the n nearest neighbours to the query.
        """
        return self.__collection.query(
            query_texts=[query], n_results=n_results, include=["documents"]
        )

    def reset_collection(self) -> None:
        """
        Clear the collection of all documents.

        Returns:
            None
        """
        self.__collection.delete()
        self.__collection = self.__create_collection__()

        return None
