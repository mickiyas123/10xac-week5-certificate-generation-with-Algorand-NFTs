import algokit_utils
import pytest
from algokit_utils import get_localnet_default_account
from algokit_utils.config import config
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient

from smart_contracts.artifacts.create_nft_certificate.client import CreateNftCertificateClient


@pytest.fixture(scope="session")
def create_nft_certificate_client(
    algod_client: AlgodClient, indexer_client: IndexerClient
) -> CreateNftCertificateClient:
    config.configure(
        debug=True,
        # trace_all=True,
    )

    client = CreateNftCertificateClient(
        algod_client,
        creator=get_localnet_default_account(algod_client),
        indexer_client=indexer_client,
    )

    client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.ReplaceApp,
        on_update=algokit_utils.OnUpdate.UpdateApp,
        allow_delete=True,
        allow_update=True,
    )
    return client


def test_says_hello(create_nft_certificate_client: CreateNftCertificateClient) -> None:
    result = create_nft_certificate_client.hello(name="World")

    assert result.return_value == "Hello, World"


def test_simulate_says_hello_with_correct_budget_consumed(
    create_nft_certificate_client: CreateNftCertificateClient, algod_client: AlgodClient
) -> None:
    result = (
        create_nft_certificate_client.compose().hello(name="World").hello(name="Jane").simulate()
    )

    assert result.abi_results[0].return_value == "Hello, World"
    assert result.abi_results[1].return_value == "Hello, Jane"
    assert result.simulate_response["txn-groups"][0]["app-budget-consumed"] < 100
