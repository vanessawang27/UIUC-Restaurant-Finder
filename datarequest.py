from yelpapi import YelpAPI
yelp_api = YelpAPI('2Jb1zx0BDdQyKjuJqsKrVA', '3Jo19wAaL23PH5YgP7OyA8Zolniw2i4ya9Dcq1LFSDYSDriEjhsDK8rk9vW5cpFs')
search_results = yelp_api.search_query(name = 'Neptune Oyster', location='Boston, MA')