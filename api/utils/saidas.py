def get_money_transaction_output(query):
    sum_outputs = 0
    
    for x in query:
        sum_outputs+=x.value_money
    
    return sum_outputs
