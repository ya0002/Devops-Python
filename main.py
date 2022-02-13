from urllib import response
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from pair_graph_query import get_pair_trade
from db import Trades,Base


if __name__ == '__main__':

    response=get_pair_trade()

    connection_string="mysql://user:root@db/main"

    engine=create_engine(connection_string,echo=True)

    Base.metadata.create_all(engine)

    Session=sessionmaker()
    local_session=Session(bind=engine)


    # add the response to MySQL db
    for trade in response:

        pair=trade['pair']
        transaction=trade['transaction']

        trade_info=Trades(
            id=trade['id'],
            timestamp=datetime.fromtimestamp(int(trade['timestamp'])),
            token1=pair['token0']['symbol'],
            token2=pair['token1']['symbol'],
            transactionCount=int(pair['txCount']),
            sender=trade['sender'],
            to=trade['to'],
            token1Price=float(pair['token0Price']),
            token1Volume=float(pair['volumeToken0']),
            token2Price=float(pair['token1Price']),
            token2Volume=float(pair['volumeToken1']),
            amount1In=float(trade['amount0In']),
            amount1Out=float(trade['amount0Out']),
            amount2In=float(trade['amount1In']),
            amount2Out=float(trade['amount1Out']),
            amountUSD=float(trade['amountUSD']),
            reserveETH=float(pair['reserveETH']),
            transactionBlockkNumber=int(transaction['blockNumber']),
            transactionID=transaction['id']
        )

        local_session.add(trade_info)
        local_session.commit()