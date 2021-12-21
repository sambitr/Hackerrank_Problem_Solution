# Link: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa3preWppSHNvUEROMEMwWEhieWlpdE1ZRzhLUXxBQ3Jtc0tsdnpobUdja3lXZUR2S0g0NEo4aE9mN19DLUpIbVAzeGkxRmo4OHdOZWdoMk9lRFAzSEdCeDA1dWs4SVpZSjlmQTB2S1Y1bDV2U2pJLS13a2I4cFVkTlZyS0RqeXFWUkk5aUpfQW1ldGNpdm1oWW84WQ&q=https%3A%2F%2Fbit.ly%2F3Il0c7n

def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    # Write your code here
    # Return a list containing all the common elements in arr and brr.
    result = []
    n = len(arr)
    m = len(brr)
    i,j = 0,0
    while((i<n) & (j<m)):
        if(arr[i] == brr[j]):
            result.append(arr[i])
            i+=1
            j+=1
        elif(arr[i] < brr[j]):
            i+=1
        else:
            j+=1
     
    return(result)
    pass
