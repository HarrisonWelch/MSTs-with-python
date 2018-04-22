for /l %%x in (1, 100, 10000) do (
   echo %%x
   python prim.py -l 10 -c -f -v -r %%x
)