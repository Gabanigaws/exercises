# # Write your code here
# ```javascript
# function median(ns)
# {
#     // In JavaScript, xs.sort() changes xs, i.e., the sorting occurs "in place"
#     // However, it isn't friendly to modify the parameter's value, so we take a copy
#     // In Python, there is a separate sorting function that does not sort in place
#     // but instead returns a new sorted list
#     // Look for this function
#     const sortedNs = [...ns]; // Make a copy
#     sortedNs.sort();

#     const i = Math.floor(ns.length / 2);

#     if ( sortedNs.length % 2 === 0 )
#     {
#         return (sortedNs[i - 1] + sortedNs[i]) / 2;
#     }
#     else
#     {
#         return sortedNs[i];
#     }
# }
# ``
def median(ns):
    sorted_ns = sorted(ns)

    i = len(sorted_ns)//2

    if len(sorted_ns) % 2 == 0:
        return (sorted_ns[i - 1] + sorted_ns[i]) / 2

    else:
        return sorted_ns[i]