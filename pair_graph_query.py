

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport


# get the payload from TheGraph
def get_pair_trade():
  sample_transport=RequestsHTTPTransport(
      url='https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2',
      verify=True,
      retries=3,
  )
  client = Client(
      transport=sample_transport
  )

  query = gql('''
  query{
    swaps(
      where:{
        pair:"0x0b4d4cd8a86cf3f51f427a811df543198c88e53d"
      }
      orderBy: timestamp
      first:1000
    ) {
      id
      timestamp
      pair{
        token0{
          symbol
        }
        token1{
          symbol
        }
        token0Price
        token1Price
        volumeToken0
        volumeToken1
        reserveETH
        txCount
    }
    sender
    amount0In
    amount1In
    amount0Out
    amount1Out
    to
    amountUSD
    transaction{
      id
      blockNumber
    }
  }
  }
  ''')

  response = client.execute(query)['swaps']
  return response


