for /l %%x in (4900, 100, 10000) do (
   echo %%x
   python kruskal_try2.py -c -f -r %%x
)