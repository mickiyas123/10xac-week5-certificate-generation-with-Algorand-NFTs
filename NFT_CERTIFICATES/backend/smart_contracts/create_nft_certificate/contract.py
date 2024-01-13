import beaker as bk
import pyteal as pt


class CertificateState:
    # ASA: ID of the ASA being transfered to the student
    asa = bk.GlobalStateValue(
        stack_type=pt.TealType.uint64, default=pt.Int(0)
        )
    # ASA amount: Total amount of asa being transfered
    asa_amount = bk.GlobalStateValue(
        stack_type=pt.TealType.uint64, default=pt.Int(0)
        )
    # Studnet to transfer to
    transfer_to = bk.GlobalStateValue(
        stack_type=pt.TealType.bytes, default=pt.Bytes("")
    )


app = bk.Application("create_nft_certificate", state=CertificateState)


@app.create(bare=True)
def create() -> pt.Expr:
    return app.initialize_global_state()


# opt_into_asset method that opts the contract account into an ASA
@app.external()
def opt_into_asset(asset: pt.abi.Asset) -> pt.Expr:
    # on chain logic that uses multiple expressions, always goes in retuned Seq
    return pt.Seq(
        # check the asa in the state hasn't been set
        pt.Assert(app.state.asa == pt.Int(0)),
        # Set app.state.asa to the asa being auctioned
        app.state.asa.set(asset.asset_id()),
        pt.InnerTxnBuilder.Execute({
            pt.TxnField.type_enum: pt.TxnType.AssetTransfer,
            pt.TxnField.asset_receiver: pt.Global.current_application_address(),
            pt.TxnField.xfer_asset: asset.asset_id(),
            pt.TxnField.asset_amount: pt.Int(0),
            pt.TxnField.fee: pt.Int(0)
        })
    )


# otp_into_app methods tha allow accounts to opt in to local state
@app.opt_in(bare=True)
def opt_in() -> pt.Expr:
    return pt.Approve()


# transfer assets(nft certificate to students)
@app.external()
def transfer_asset(payment: pt.abi.PaymentTransaction, axfer: pt.abi.AssetTransferTransaction) -> pt.Expr:
    return pt.Seq(
        app.state.asa_amount.set(axfer.get().asset_amount()),
        app.state.transfer_to.set(payment.get().sender()),
        # send asset to student
        pt.InnerTxnBuilder.Execute({
            pt.TxnField.type_enum: pt.TxnType.AssetTransfer,
            pt.TxnField.asset_receiver: app.state.transfer_to.get(),
            pt.TxnField.xfer_asset: app.state.asa.get(),
            pt.TxnField.asset_amount: app.state.asa_amount.get(),
            pt.TxnField.asset_close_to: app.state.asa_amount.get(),
            pt.TxnField.fee: pt.Int(0)
        })
    )


def delete() -> pt.Expr:
    return pt.Seq(
        
    )

@app.external
def hello(name: pt.abi.String, *, output: pt.abi.String) -> pt.Expr:
    return output.set(pt.Concat(pt.Bytes("Hello, "), name.get()))




