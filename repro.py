import asyncio

import weaviate.classes.config as wvcc
from weaviate import WeaviateAsyncClient
from weaviate.collections.classes.filters import Filter
from weaviate.connect import ConnectionParams


async def main():
    async with WeaviateAsyncClient(
        ConnectionParams.from_params(
            http_host="weaviate",
            http_port=80,
            http_secure=False,
            grpc_host="weaviate-grpc",
            grpc_port=50051,
            grpc_secure=False,
        )
    ) as client:
        await client.collections.delete_all()
        test_col = await client.collections.create(
            "test",
            properties=[
                wvcc.Property(
                    name="index", data_type=wvcc.DataType.INT, tokenization=None
                )
            ],
        )
        await asyncio.sleep(2)

        response = await test_col.data.insert_many([{"index": i} for i in range(200)])
        print("created:", len(response.uuids))

        response = await test_col.query.fetch_objects(
            filters=Filter.by_id().contains_any(response.uuids.values()),
        )

        print("returned:", len(response.objects))


asyncio.run(main())
