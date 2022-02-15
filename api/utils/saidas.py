def get_amount_transaction_output(query):
    sum_outputs = 0
    
    for x in query:
        sum_outputs+=x.amount
    
    return sum_outputs
