def get_amount_transaction_input(query):
    sum_inputs = 0
    
    for x in query:
        sum_inputs+=x.amount
    
    return sum_inputs
