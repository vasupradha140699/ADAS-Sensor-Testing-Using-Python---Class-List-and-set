class Adas_sensor:
    def __init__(self, sensor_Id, sensor_type, detection_range):
         print(f"_______________Test cases________________")
         self.sensor_Id = sensor_Id
         self.sensor_type = sensor_type
         self.detection_range = detection_range
        #  self.test results = test results
    def display_details(self):
         print(f"Sensor_ID: {self.sensor_Id}")
         print(f"Sensor_Type: {self.sensor_type}")
         print(f"detection_range = {self.detection_range}")
    def check_detection_range(self):
        if self.detection_range >= 100:
            print("Long range sensor")
        else:
            print("short range sensor")
    def test_results(self):
        if self.sensor_type == "camera":
            if 10<=self.detection_range<=100:
                print("Test result = PASS")
                return "PASS"
            else:
                print("Test result = FAIL")
                return "FAIL"
               
        if self.sensor_type == "Lidar":
            if 0<=self.detection_range<=10:
                print("Test result = PASS")
                return "PASS"
               
            else:
                print("Test result = FAIL")
                return "FAIL"
                
        if self.sensor_type == "ultrasonic":
            if 0<=self.detection_range<=5:
                print("Test result = PASS")
                return "PASS"
                
            else:
                print("Test result = FAIL")
                return "FAIL"

sensor_List = [
    (201,"camera",80),
    (202,"Lidar",90),
    (203,"ultrasonic",80),
    (204,"camera",150),
    (205,"Lidar",10)
]
count = 1
for sensor_Id, sensor_type,detection_range in sensor_List:  
    a1 = Adas_sensor(sensor_Id, sensor_type,detection_range)
    a1.display_details()
    count +=1
    a1.test_results()
    a1.check_detection_range()
index = 5
print("--------------adding sensor ID 206 : camera to the list------")
sensor_List.append((206,"camera",100))
print(sensor_List)
print("----------sensor with detection range above 80 m------------")
countp = 0
countf = 0
for sensor_Id, sensor_type,detection_range in sensor_List: 
    if detection_range>=80:
        print(f"{sensor_type}={detection_range}")
for sensor_Id, sensor_type,detection_range in sensor_List: 
    if sensor_type == "camera":
        result = "PASS" if 10 <= detection_range <= 100 else "FAIL"
    if sensor_type == "Lidar":
        result = "PASS" if 0<=detection_range<=10 else "FAIL"
    if sensor_type == "ultrasonic":
        result = "PASS" if 0<=detection_range<=5 else "FAIL"
    if result == "PASS":
        countp += 1
    if result == "FAIL":
        countf +=1
print("_____________passed and failed count______________________")
print("Passed count :",countp)
print("Failed count :",countf)
List = []
Listp = []
for sensor_Id, sensor_type,detection_range in sensor_List: 
    if sensor_type == "camera":
        result = "PASS" if 10 <= detection_range <= 100 else "FAIL"
    if sensor_type == "Lidar":
        result = "PASS" if 0<=detection_range<=10 else "FAIL"
    if sensor_type == "ultrasonic":
        result = "PASS" if 0<=detection_range<=5 else "FAIL"
    if result == "FAIL":
       List.append(sensor_Id)
       res = List
    if result == "PASS":
        Listp.append(sensor_Id)
        resp = Listp
print("-----------------Failed sensor ID -------------------------")
print("Failed sensor ID:", res)
print("-----------------Passed sensor ID -------------------------")
print("Passed sensor ID:", resp)
index = 0
for item in sensor_List:
    if item[0] == 203:
        sensor_List[index] = (item[0], item[1], 5)
    index = index +1
print("_______________Changing detection_range of 203 sensor ID----------------")
print(sensor_List)
new = 0
index = 0
print("------------------deleting the sensor ID 204----------------")
for item in sensor_List:
    if item[0] == 204:
        sensor_List.remove(item)
print(sensor_List)
print()
print("-----------------------------creating set-------------------------------------")
sensor_ids = {201, 202, 203, 201, 204, 205}
print("------------------printing set so duplicates are deleted-----------------------")
print(sensor_ids)
print("------------------Adding sensor ID 206 to the set-----------------------------")
sensor_ids.add(206)
print(sensor_ids)
print("-------------------deleting sensor ID 204 from the set------------------------")
sensor_ids.discard(204)
print("After removing 204",sensor_ids)
print("-----------------checking whether sensor ID 203 exists in the set--------------")
if 203 in sensor_ids:
    print("sensor ID  : 203 is present in the set")
else:
    print("sensor ID  : 203 is not present in the set")
print("-----------------printing the number of unique IDs---------------------------")
print(len(sensor_ids))
failed_Sensor_ids = set()
print("---------------printing the IDs of passed and failed sensor in set-------------")
for item in sensor_List:
    # res and resp is a list containing passed and failed sensor ids
    failed_Sensor_ids= set(res)
    passed_sensor_ids = set(resp)
print("Failed sensor ID's:",failed_Sensor_ids)
print("Passed sensor ID's:",passed_sensor_ids)
print("-------------------printing all the sensor IDs from list--------------------")
New1 =[item[0] for item in sensor_List]
print("sensor IDs from list:",New1)
New = set(New1)
print("------------------printing all the sensor IDs from set---------------------")
print("sensor IDs in set:",sensor_ids)
print("------------------printing the union of both list and set------------------")
print("Union:",New |sensor_ids)
print("------------------printing the intersection of both list and set-----------")
print("Intersection:",New&sensor_ids)
print("-----------------printing the difference between both list and set---------")
print("List Ids missing from set:",New-sensor_ids)
print("Set IDs missing from List:",sensor_ids-New)
   
 