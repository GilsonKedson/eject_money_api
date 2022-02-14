def get_money_transaction_input(query):
    sum_inputs = 0
    
    for x in query:
        sum_inputs+=x.value_money
    
    return sum_inputs
