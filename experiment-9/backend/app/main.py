from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="CareFlow API", version="1.0.0", description="Synthetic healthcare demo API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["GET"], allow_headers=["*"])

patients = [
 {"id":"PT-1001","name":"Aarav Mehta","age":34,"gender":"Male","blood_group":"O+","condition":"Hypertension","status":"Active","last_visit":"2026-11-10","doctor":"Dr. Ananya Rao"},
 {"id":"PT-1002","name":"Diya Sharma","age":27,"gender":"Female","blood_group":"B+","condition":"Migraine","status":"Active","last_visit":"2026-11-11","doctor":"Dr. Kabir Singh"},
 {"id":"PT-1003","name":"Ishaan Verma","age":52,"gender":"Male","blood_group":"AB+","condition":"Type 2 Diabetes","status":"Under Review","last_visit":"2026-11-08","doctor":"Dr. Ananya Rao"},
 {"id":"PT-1004","name":"Meera Iyer","age":41,"gender":"Female","blood_group":"A+","condition":"Thyroid Disorder","status":"Active","last_visit":"2026-11-12","doctor":"Dr. Rhea Kapoor"},
 {"id":"PT-1005","name":"Vivaan Patel","age":19,"gender":"Male","blood_group":"O-","condition":"Seasonal Allergy","status":"Discharged","last_visit":"2026-11-06","doctor":"Dr. Kabir Singh"},
 {"id":"PT-1006","name":"Sara Khan","age":63,"gender":"Female","blood_group":"B-","condition":"Cardiac Follow-up","status":"Under Review","last_visit":"2026-11-12","doctor":"Dr. Rhea Kapoor"},
]
doctors = [
 {"id":"DR-01","name":"Dr. Ananya Rao","specialty":"Cardiology","availability":"Available","patients":18},
 {"id":"DR-02","name":"Dr. Kabir Singh","specialty":"Neurology","availability":"In consultation","patients":14},
 {"id":"DR-03","name":"Dr. Rhea Kapoor","specialty":"Endocrinology","availability":"Available","patients":21},
]
appointments = [
 {"id":"APT-2401","patient":"Aarav Mehta","patient_id":"PT-1001","doctor":"Dr. Ananya Rao","time":"09:00 AM","type":"Follow-up","status":"Confirmed","date":"2026-11-13"},
 {"id":"APT-2402","patient":"Diya Sharma","patient_id":"PT-1002","doctor":"Dr. Kabir Singh","time":"09:30 AM","type":"Consultation","status":"Checked in","date":"2026-11-13"},
 {"id":"APT-2403","patient":"Ishaan Verma","patient_id":"PT-1003","doctor":"Dr. Ananya Rao","time":"10:15 AM","type":"Review","status":"Confirmed","date":"2026-11-13"},
 {"id":"APT-2404","patient":"Meera Iyer","patient_id":"PT-1004","doctor":"Dr. Rhea Kapoor","time":"11:00 AM","type":"Consultation","status":"Pending","date":"2026-11-13"},
 {"id":"APT-2405","patient":"Sara Khan","patient_id":"PT-1006","doctor":"Dr. Rhea Kapoor","time":"11:45 AM","type":"Cardiac review","status":"Confirmed","date":"2026-11-13"},
]

@app.get("/health")
def health(): return {"status":"healthy","service":"careflow-api"}

@app.get("/api/overview")
def overview():
 return {"patients":len(patients),"appointments_today":len(appointments),"doctors_available":2,"needs_attention":2,
 "weekly_visits":[{"day":"Mon","visits":28},{"day":"Tue","visits":35},{"day":"Wed","visits":31},{"day":"Thu","visits":42},{"day":"Fri","visits":38},{"day":"Sat","visits":24},{"day":"Sun","visits":18}],
 "department_load":[{"department":"Cardiology","visits":32},{"department":"Neurology","visits":26},{"department":"Endocrine","visits":21},{"department":"General","visits":18}]}

@app.get("/api/patients")
def get_patients(): return patients
@app.get("/api/doctors")
def get_doctors(): return doctors
@app.get("/api/appointments")
def get_appointments(): return appointments
@app.get("/api/records")
def get_records():
 return [
  {"id":"MR-8101","patient":"Aarav Mehta","category":"Blood Pressure","date":"2026-11-10","result":"128/82 mmHg","flag":"Normal"},
  {"id":"MR-8102","patient":"Ishaan Verma","category":"HbA1c","date":"2026-11-08","result":"7.2%","flag":"Review"},
  {"id":"MR-8103","patient":"Sara Khan","category":"ECG","date":"2026-11-12","result":"Sinus rhythm","flag":"Normal"},
  {"id":"MR-8104","patient":"Meera Iyer","category":"TSH","date":"2026-11-12","result":"5.1 mIU/L","flag":"Review"}]
