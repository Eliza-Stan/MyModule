def top_n(items,n):
    """
    Sorts an array like object or list of numbers into descending order and returns the n top items
    of the newly sorted list.

    Args:
        items (array): array or list of numbers
        n (int) : the number of items to return

    Returns:
        (array) : an array of the n items in descending order

    Example:
        >>>top_n ([8,4,2,5,7,1], 3) 
        [8,7,5]
    """

    for i in range(n): #keep sorting until we have n items in an array
        for j in range(len(items)-1-i):

            if items[j]>items[j+1]: #if this item is bigger than the next...
                items[j], items[j+1] = items[j+1], items[j] #swap the two numbers

    top_n = items[-n:] #gets the top n items.

    return top_n[::-1] #returns in descending order


