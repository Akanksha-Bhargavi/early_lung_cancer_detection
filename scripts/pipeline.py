import logging
from scripts.utils import connect_to_mongo
from scripts.utils import DATA_PATH, CLIENT, DB, COLLECTION

def peer_pressure_analysis():
    pipeline = [
        {"$match": {"PEER_PRESSURE": {"$in": [1, 2]}}},
        {"$group": {"_id": {"gender": "$GENDER", "peer_pressure": "$PEER_PRESSURE"},
                    "total": {"$sum": 1},
                    "smokers": {"$sum": {"$cond": [{"$eq": ["$SMOKING", 1]}, 1, 0]}}}},
        {"$project": {"gender": "$_id.gender",
                      "peer_pressure": "$_id.peer_pressure",
                      "total": 1,
                      "smokers": 1,
                      "smoking_percentage": {"$multiply": [{"$divide": ["$smokers", "$total"]}, 100]}}},
        {"$sort": {"gender": 1, "peer_pressure": 1}}
    ]
    results = list(COLLECTION.aggregate(pipeline))
    print("\n \nINFLUENCE OF PEER PRESSURE ON SMOKING BY GENDER:")
    for result in results:
        print(f"Gender: {result['gender']}, Peer Pressure Level: {result['peer_pressure']}")
        print(f"  Total Individuals: {result['total']}")
        print(f"  Smokers: {result['smokers']}")
        print(f"  Smoking Percentage: {result['smoking_percentage']:.2f}%")
        print("-" * 34)


def lc_gender():
    pipeline = [
        { '$group': { '_id': { 'gender': '$GENDER', 'smoking': '$SMOKING' },
                      'total': { '$sum': 1 },
                      'lung_cancer_yes': { '$sum': { '$cond': [ { '$eq': ['$LUNG_CANCER', 'YES'] }, 1, 0 ] } } } },
        { '$project': { 'gender': '$_id.gender', 'smoking': '$_id.smoking', 'total': 1,
                        'lung_cancer_yes': 1,
                        'lung_cancer_percentage': { '$multiply': [ { '$divide': ['$lung_cancer_yes', '$total'] }, 100 ] } } },
        { '$sort': { 'gender': 1, 'smoking': 1 } }
    ]
    results = list(COLLECTION.aggregate(pipeline))
    print("LUNG CANCER IN SMOKERS BY GENDER:")
    for result in results:
        smoking_status = 'Smoker' if result['smoking'] == 1 else 'Non-Smoker'
        print(f"Gender: {result['gender']}, Smoking Status: {smoking_status}")
        print(f"  Total: {result['total']}, Lung Cancer (YES): {result['lung_cancer_yes']}")
        print(f"  Lung Cancer Percentage: {result['lung_cancer_percentage']:.2f}%")
        print('-' * 34)


        



def lung_cancer_chronic_disease():
    pipeline = [
        {"$group": {"_id": {"gender": "$GENDER", "chronic_disease": "$CHRONIC_DISEASE"},
                    "total": {"$sum": 1},
                    "lung_cancer_yes": {"$sum": {"$cond": [{"$eq": ["$LUNG_CANCER", "YES"]}, 1, 0]}},
                    "lung_cancer_no": {"$sum": {"$cond": [{"$eq": ["$LUNG_CANCER", "NO"]}, 1, 0]}}}},
        {"$project": {"gender": "$_id.gender",
                      "chronic_disease": "$_id.chronic_disease",
                      "total": 1,
                      "lung_cancer_yes": 1,
                      "lung_cancer_no": 1,
                      "lung_cancer_percentage": {"$multiply": [{"$divide": ["$lung_cancer_yes", "$total"]}, 100]}}},
        {"$sort": {"gender": 1, "chronic_disease": 1}}
    ]
    results = list(COLLECTION.aggregate(pipeline))
    print("LUNG CANCER IN INDIVIDUALS WITH CHRONIC DISEASE:")
    for result in results:
        disease_severity = "Mild" if result['chronic_disease'] == 1 else "Severe"
        print(f"Gender: {result['gender']}, Chronic Disease Severity: {disease_severity}")
        print(f"  Total Individuals: {result['total']}")
        print(f"  Lung Cancer (YES): {result['lung_cancer_yes']}")
        print(f"  Lung Cancer (NO): {result['lung_cancer_no']}")
        print(f"  Lung Cancer Percentage: {result['lung_cancer_percentage']:.2f}%")
        print("-" * 34)



def lc_smokers_chronic_disease():
    pipeline = [
        {"$match": {"SMOKING": 1, "CHRONIC_DISEASE": {"$in": [1, 2]}}},
        {"$group": {"_id": {"gender": "$GENDER", "lung_cancer": "$LUNG_CANCER"},
                    "total": {"$sum": 1}}},
        {"$group": {"_id": "$_id.gender",
                    "total": {"$sum": "$total"},
                    "lung_cancer_yes": {"$sum": {"$cond": [{"$eq": ["$_id.lung_cancer", "YES"]}, "$total", 0]}}}},
        {"$project": {"gender": "$_id",
                      "total": 1,
                      "lung_cancer_yes": 1,
                      "lung_cancer_percentage": {"$multiply": [{"$divide": ["$lung_cancer_yes", "$total"]}, 100]}}},
        {"$sort": {"gender": 1}}
    ]
    results = list(COLLECTION.aggregate(pipeline))
    print("SMOKERS WITH LUNG CANCER AND CHRONIC DISEASE:")
    for result in results:
        print(f"Gender: {result['gender']}")
        print(f"  Total Smokers with Chronic Disease: {result['total']}")
        print(f"  Lung Cancer (YES): {result['lung_cancer_yes']}")
        print(f"  Lung Cancer Percentage: {result['lung_cancer_percentage']:.2f}%")
        print("-" * 34)
        

peer_pressure_analysis()
print("-" * 34)
print("\n \n \n")
lc_gender()
print("-" * 34)
print("\n \n \n")
lung_cancer_chronic_disease()
print("-" * 34)
print("\n \n \n")
lc_smokers_chronic_disease()
print("-" * 34)
