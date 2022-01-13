#!/usr/bin/env python
# coding: utf-8

# In[63]:


import requests

token = "eyJ0eXAiOiJKV1QiLCJub25jZSI6Ik5LRGZfcG95cVNKdER4QTFfVWh1UUxVWllrSmVjdDdDeTZrTTE1eXVWZHciLCJhbGciOiJSUzI1NiIsIng1dCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyIsImtpZCI6Im5PbzNaRHJPRFhFSzFqS1doWHNsSFJfS1hFZyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNjIzODI2NjY2LCJuYmYiOjE2MjM4MjY2NjYsImV4cCI6MTYyMzgzMDU2NiwiYWNjdCI6MCwiYWNyIjoiMSIsImFjcnMiOlsidXJuOnVzZXI6cmVnaXN0ZXJzZWN1cml0eWluZm8iLCJ1cm46bWljcm9zb2Z0OnJlcTEiLCJ1cm46bWljcm9zb2Z0OnJlcTIiLCJ1cm46bWljcm9zb2Z0OnJlcTMiLCJjMSIsImMyIiwiYzMiLCJjNCIsImM1IiwiYzYiLCJjNyIsImM4IiwiYzkiLCJjMTAiLCJjMTEiLCJjMTIiLCJjMTMiLCJjMTQiLCJjMTUiLCJjMTYiLCJjMTciLCJjMTgiLCJjMTkiLCJjMjAiLCJjMjEiLCJjMjIiLCJjMjMiLCJjMjQiLCJjMjUiXSwiYWlvIjoiQVVRQXUvOFRBQUFBTzNRWlhqNm5tdXIydU1wNFBaR0xKaDkxZzdPK3hQTyszZEdGeVdxN2VzV0lBZ3BWT2Izd0p2NEhSc0U3NER2MVZVVzhNL2FKU3hwR2V2b21qeUxObWc9PSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggZXhwbG9yZXIgKG9mZmljaWFsIHNpdGUpIiwiYXBwaWQiOiJkZThiYzhiNS1kOWY5LTQ4YjEtYThhZC1iNzQ4ZGE3MjUwNjQiLCJhcHBpZGFjciI6IjAiLCJmYW1pbHlfbmFtZSI6IkxvcmVuem8iLCJnaXZlbl9uYW1lIjoiTWF0aGlzIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiOTIuMTY3LjQxLjIxMyIsIm5hbWUiOiJNYXRoaXMgTG9yZW56byIsIm9pZCI6IjRjOGI0YjdiLThhNTItNDg3NC05NGFkLWM4NDk4NjE5OGVlZiIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTUyNDM1Mjc3LTE1OTY0OTU3OTUtMzA4OTYxMzczMS0zNzY2NiIsInBsYXRmIjoiMTQiLCJwdWlkIjoiMTAwMzIwMDA3QTRCQUE3MCIsInJoIjoiMC5BWFFBeXJRY2tHSzRLVUNUQnVYTkQyMmZoclhJaTk3NTJiRklxSzIzU05weVVHUjBBR2cuIiwic2NwIjoiR3JvdXAuUmVhZC5BbGwgR3JvdXAuUmVhZFdyaXRlLkFsbCBwcm9maWxlIG9wZW5pZCBlbWFpbCBVc2VyLlJlYWQiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiJSQW50TW55MmJVQ1hDaTIxSndCWXIwQXN5SG9CRTdzUVhrTVg0UmMtRTNjIiwidGVuYW50X3JlZ2lvbl9zY29wZSI6IkVVIiwidGlkIjoiOTAxY2I0Y2EtYjg2Mi00MDI5LTkzMDYtZTVjZDBmNmQ5Zjg2IiwidW5pcXVlX25hbWUiOiJtYXRoaXMubG9yZW56b0BlcGl0ZWNoLmV1IiwidXBuIjoibWF0aGlzLmxvcmVuem9AZXBpdGVjaC5ldSIsInV0aSI6IjlJTHl3dWFaMUVTXzA1Q0x6WFlPQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfc3QiOnsic3ViIjoiNkpfTWhOTGh4SGhvd1BIWjF5NV9aWjNWaDZsNUJyLVRsQWtlNm8weEZiQSJ9LCJ4bXNfdGNkdCI6MTQxNzgwNDg4N30.lokMi4gLhLkLY4uo06kiDyEbc1V3yj7W28tySAABD955IsSYcq8AZo3gG8kUKVy5Ge2-JvtGIUS-3TypIe3m4llRmFKEPO-RvKUOYjeZyjf4XG9WQ8Ql_Gyj8gvhm3c9ugvFRxaGByeS_HTxSvArmg2Qk7e1pQ7GBpbzxwS3FkYCg3L3V9jg9jPjTn3bnginLlRINpFc_QXX2-RkX1xwSGQKerzTi7xvjt3xvO0yuFRN-m_kvJzI7Tbt-jyIrjf2TQVHftWYWAVX-pF9i4tbOFfuhyPSO7FzUjZsk6UxA3ehAaJUzmig4n6wkswyLK--jDOuqz4B8-YfJvUksCymYQ"


# In[64]:


url = f"https://graph.microsoft.com/beta/me/memberOf/"


# In[69]:


def member_of():
    res = {}
    url = f"https://graph.microsoft.com/beta/me/memberOf/"
    content = requests.get(url, headers={'Authorization': token})
    data = content.json()
    for i in data['value']:
        res[i['displayName']] = i['id']
    return res

teams = member_of()
for name, id in teams.items():
    print(name, id)


# In[ ]:




