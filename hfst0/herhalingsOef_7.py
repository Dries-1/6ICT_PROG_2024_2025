def seconden_per_dag(aantal):
    """ return de seconden in 'aantal' dagen 
            Tip! een dag is 24u, 
                 een uur is 60min, 
                 een minuut is 60s
    """
    seconden_per_dag = 24 * 60 * 60
    return aantal * seconden_per_dag

print(seconden_per_dag(1))    # 86400
print(seconden_per_dag(3))    # 259200
print(seconden_per_dag(7))    # 604800