import pandas as pd


def process_data():
    # Do not alter this line.
    biopics = pd.read_csv("biopics.csv", encoding='latin-1')
    # Write your code here.
    biopics = biopics.drop_duplicates() # filter out duplicated rows
    biopics = biopics.rename(columns={'box_office': 'earnings'}) # rename box_office to earnings
    biopics = biopics.dropna(axis='rows', subset=['earnings']) # filter out rows for which earnings are missing
    biopics = biopics[biopics['year_release'] >= 1990] # keep only movies released in the year 1990 or later
    biopics['type_of_subject'] = biopics['type_of_subject'].astype("category") # convert type_of_subject to category
    biopics['country'] = biopics['country'].astype("category") # convert country to category
    biopics['lead_actor_actress_known'] = biopics['lead_actor_actress'].notna() # lead_actor_actress_known is False if lead_actor_actress is NaN and True otherwise
    biopics['earnings'] = biopics['earnings'].truediv(1000000) # update earnings expressed in millions
    biopics = biopics[['title', 'year_release', 'earnings', 'country', 'type_of_subject', 'lead_actor_actress', 'lead_actor_actress_known']] # reorder columns
    biopics = biopics.sort_values(by = 'earnings', axis='index', ascending=False) # sort by earnings descending

    # Remember to return the right object.
    return biopics.reset_index(drop=True)


if __name__ == '__main__':
    # import timeit
    # print(timeit.timeit('solution(A)', setup='from __main__ import solution; import numpy; A = numpy.random.randint(-1000000,1000000,100000)', number=10000))
    process_data()