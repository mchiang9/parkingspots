##
#1
Standard get function
Gets everything in range that is not reserved
Test #1:
curl -X GET localhost:8000/api/v1/parkingspots/available/37.5/-122.4/20.0

Result #1:
[{"id": 1, "lat": "37.50", "lon": "-122.40"}, {"id": 2, "lat": "37.50", "lon": "-121.40"}, {"id": 3, "lat": "37.50", "lon": "-120.40"}, {"id": 4, "lat": "37.50", "lon": "-119.40"}, {"id": 5, "lat": "36.50", "lon": "-122.40"}, {"id": 6, "lat": "37.50", "lon": "-122.50"}, {"id": 9, "lat": "37.50", "lon": "-105.00"}]

#2
Standard post function
This will change any spots with id 1 to become reserved
Test #2:
curl -X POST localhost:8000/api/v1/parkingspots/reserve/3

Result #2:
{"reserved": "true"}

#3
Testing the post and get function
The database should be updated so the same output as Test #1 should happen but the first result with id:1 should not be there
Test #3:
curl -X GET localhost:8000/api/v1/parkingspots/available/37.5/-122.4/20.0

Result #4:
[{"id": 1, "lat": "37.50", "lon": "-122.40"}, {"id": 2, "lat": "37.50", "lon": "-121.40"}, {"id": 4, "lat": "37.50", "lon": "-119.40"}, {"id": 5, "lat": "36.50", "lon": "-122.40"}, {"id": 6, "lat": "37.50", "lon": "-122.50"}, {"id": 9, "lat": "37.50", "lon": "-105.00"}]

#4
Test to make sure nothing is in range, except the spot it’s on
Radius = 0
Test#4:
curl -X GET localhost:8000/api/v1/parkingspots/available/37.5/-122.4/0

Result #4:
[{"id": 1, "lat": "37.50", "lon": "-122.40"}]
