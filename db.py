from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,DateTime,Integer,Float,BigInteger

Base=declarative_base()


""""
class Trades
    'id': '0x6c9cc5854a6c6d328298cab80c0cda665a517cfb727bfdc7358ada969884aa54-0',

    'amount0In': '0.1',
    'amount0Out': '0',
    'amount1In': '0',
    'amount1Out': '5610228835.813430036263598849',
    'amountUSD': '136.8287023980023743218307292936314',
    
    'pair': {'reserveETH': '0.000000000000000001',

            'token0': {'symbol': 'WETH'},
            'token0Price': '0.000000003944053179688376966387086803881565',
            'volumeToken0': '0.259303003083113681'

            'token1': {'symbol': 'UNI'},
            'token1Price': '253546277',
            'volumeToken1': '14905797851.613429874220853528'},

            'txCount': '6',


    'sender': '0x7a250d5630b4cf539739df2c5dacb4c659f2488d',
    'timestamp': '1622771111',
    'to': '0x9b85699f03916f6be3598642cfdbac2431378ccf',

    'transaction': {'blockNumber': '12565066',
                    'id': '0x6c9cc5854a6c6d328298cab80c0cda665a517cfb727bfdc7358ada969884aa54'}}

"""

class Trades(Base):
    __tablename__='trades'
    id=Column(String(300),primary_key=True)
    timestamp=Column(DateTime())

    token1=Column(String(5))
    token2=Column(String(5))

    transactionCount=Column(Integer())

    sender=Column(String(300))
    to=Column(String(300))

    token1Price=Column(Float())
    token1Volume=Column(Float())

    token2Price=Column(Float())
    token2Volume=Column(Float())

    amount1In=Column(Float())
    amount1Out=Column(Float())

    amount2In=Column(Float())
    amount2Out=Column(Float())

    amountUSD=Column(Float())

    reserveETH=Column(Float())

    transactionBlockkNumber=Column(BigInteger())
    transactionID=Column(String(300))
