import math

patients = [
    # [id, age, systolic_bp, heart_rate, blood_glucose, oxygen_sat, readmitted]
    # readmitted: 1 = yes (within 30 days), 0 = no
    ["P001", 72, 185, 110, 280, 91, 1],
    ["P002", 45, 120, 78, 95, 98, 0],
    ["P003", 60, 175, 102, 240, 93, 1],
    ["P004", 33, 115, 72, 88, 99, 0],
    ["P005", 81, 195, 118, 310, 88, 1],
    ["P006", 55, 130, 85, 110, 97, 0],
    ["P007", 67, 160, 95, 200, 94, 1],
    ["P008", 29, 110, 68, 82, 99, 0],
    ["P009", 74, 190, 115, 295, 89, 1],
    ["P010", 50, 125, 80, 105, 98, 0],
    ["P011", 63, 170, 98, 220, 92, 1],
    ["P012", 38, 118, 74, 90, 99, 0],
    ["P013", 78, 200, 122, 330, 86, 1],
    ["P014", 44, 122, 76, 98, 98, 0],
    ["P015", 70, 178, 108, 260, 90, 1],
]

# Helper functions for basic statistics
def calculate_mean(values):
    """Calculate mean from scratch"""
    return sum(values) / len(values)

def calculate_std(values):
    """Calculate population standard deviation from scratch"""
    mean = calculate_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

def calculate_min(values):
    """Calculate minimum from scratch"""
    min_val = values[0]
    for val in values:
        if val < min_val:
            min_val = val
    return min_val

def calculate_max(values):
    """Calculate maximum from scratch"""
    max_val = values[0]
    for val in values:
        if val > max_val:
            max_val = val
    return max_val


# TASK 1: Patient Data Profiler
def profile_patients(patients):
    """Task 1: Print patient profile report with statistics"""
    print("=== PATIENT PROFILE REPORT ===")
    
    # Count readmitted vs not readmitted
    total = len(patients)
    readmitted = sum(1 for p in patients if p[6] == 1)
    not_readmitted = total - readmitted
    readmission_rate = (readmitted / total) * 100
    
    print(f"Total Patients : {total} | Readmitted: {readmitted} | Not Readmitted: {not_readmitted}")
    print(f"Readmission Rate: {readmission_rate:.2f}%")
    print()
    print("Vital Signs Summary:")
    
    # Extract vital sign columns
    systolic_bp_vals = [p[2] for p in patients]
    heart_rate_vals = [p[3] for p in patients]
    blood_glucose_vals = [p[4] for p in patients]
    oxygen_sat_vals = [p[5] for p in patients]
    
    # Calculate and print statistics for each vital sign
    vitals = [
        ("systolic_bp", systolic_bp_vals),
        ("heart_rate", heart_rate_vals),
        ("blood_glucose", blood_glucose_vals),
        ("oxygen_sat", oxygen_sat_vals)
    ]
    
    for name, values in vitals:
        mean_val = calculate_mean(values)
        std_val = calculate_std(values)
        min_val = calculate_min(values)
        max_val = calculate_max(values)
        print(f"{name} : mean={mean_val:.2f}, std={std_val:.2f}, min={min_val}, max={max_val}")
    
    print()


# TASK 2: Composite Risk Scoring
def risk_score(patients):
    """Task 2: Compute risk scores and classify patients"""
    print("=== RISK ASSESSMENT REPORT ===")
    
    # Extract vital sign columns
    systolic_bp_vals = [p[2] for p in patients]
    heart_rate_vals = [p[3] for p in patients]
    blood_glucose_vals = [p[4] for p in patients]
    oxygen_sat_vals = [p[5] for p in patients]
    
    # Get min and max for each vital sign
    bp_min, bp_max = calculate_min(systolic_bp_vals), calculate_max(systolic_bp_vals)
    hr_min, hr_max = calculate_min(heart_rate_vals), calculate_max(heart_rate_vals)
    glucose_min, glucose_max = calculate_min(blood_glucose_vals), calculate_max(blood_glucose_vals)
    oxygen_min, oxygen_max = calculate_min(oxygen_sat_vals), calculate_max(oxygen_sat_vals)
    
    # Step 1: Normalize each vital sign using min-max normalization
    # Step 2: Invert oxygen saturation
    # Step 3: Compute weighted composite risk score
    risk_dict = {}
    patient_risks = []
    
    for patient in patients:
        patient_id = patient[0]
        age = patient[1]
        systolic_bp = patient[2]
        heart_rate = patient[3]
        blood_glucose = patient[4]
        oxygen_sat = patient[5]
        
        # Min-max normalization
        bp_norm = (systolic_bp - bp_min) / (bp_max - bp_min) if bp_max != bp_min else 0
        hr_norm = (heart_rate - hr_min) / (hr_max - hr_min) if hr_max != hr_min else 0
        glucose_norm = (blood_glucose - glucose_min) / (glucose_max - glucose_min) if glucose_max != glucose_min else 0
        oxygen_norm = (oxygen_sat - oxygen_min) / (oxygen_max - oxygen_min) if oxygen_max != oxygen_min else 0
        
        # Invert oxygen saturation
        oxygen_risk = 1 - oxygen_norm
        
        # Weighted composite risk score
        risk = 0.30 * bp_norm + 0.25 * hr_norm + 0.25 * glucose_norm + 0.20 * oxygen_risk
        
        # Classify
        if risk >= 0.70:
            category = "CRITICAL"
        elif risk >= 0.40:
            category = "MODERATE"
        else:
            category = "STABLE"
        
        risk_dict[patient_id] = (risk, category)
        patient_risks.append((patient_id, age, risk, category))
    
    # Sort by risk score descending (highest first)
    patient_risks.sort(key=lambda x: x[2], reverse=True)
    
    # Print sorted results
    for patient_id, age, risk, category in patient_risks:
        print(f"{patient_id} | Age: {age} | Risk: {risk:.3f} | {category}")
    
    print()
    return risk_dict


# TASK 3: Vital Sign Breach Detector
def breach_detector(patients):
    """Task 3: Identify patients with extreme vital signs using z-score"""
    print("=== VITAL SIGN BREACH ALERTS ===")
    
    # Extract vital sign columns
    systolic_bp_vals = [p[2] for p in patients]
    heart_rate_vals = [p[3] for p in patients]
    blood_glucose_vals = [p[4] for p in patients]
    oxygen_sat_vals = [p[5] for p in patients]
    
    # Calculate means and standard deviations
    bp_mean = calculate_mean(systolic_bp_vals)
    bp_std = calculate_std(systolic_bp_vals)
    
    hr_mean = calculate_mean(heart_rate_vals)
    hr_std = calculate_std(heart_rate_vals)
    
    glucose_mean = calculate_mean(blood_glucose_vals)
    glucose_std = calculate_std(blood_glucose_vals)
    
    oxygen_mean = calculate_mean(oxygen_sat_vals)
    oxygen_std = calculate_std(oxygen_sat_vals)
    
    # Check for breaches
    breached_patients = []
    
    for patient in patients:
        patient_id = patient[0]
        systolic_bp = patient[2]
        heart_rate = patient[3]
        blood_glucose = patient[4]
        oxygen_sat = patient[5]
        
        breaches = []
        
        # Z-score for systolic_bp (dangerous if z > +1.5)
        bp_z = (systolic_bp - bp_mean) / bp_std if bp_std != 0 else 0
        if bp_z > 1.5:
            breaches.append(f"systolic_bp (z=+{bp_z:.2f})")
        
        # Z-score for heart_rate (dangerous if z > +1.5)
        hr_z = (heart_rate - hr_mean) / hr_std if hr_std != 0 else 0
        if hr_z > 1.5:
            breaches.append(f"heart_rate (z=+{hr_z:.2f})")
        
        # Z-score for blood_glucose (dangerous if z > +1.5)
        glucose_z = (blood_glucose - glucose_mean) / glucose_std if glucose_std != 0 else 0
        if glucose_z > 1.5:
            breaches.append(f"blood_glucose (z=+{glucose_z:.2f})")
        
        # Z-score for oxygen_sat (dangerous if z < -1.5)
        oxygen_z = (oxygen_sat - oxygen_mean) / oxygen_std if oxygen_std != 0 else 0
        if oxygen_z < -1.5:
            breaches.append(f"oxygen_sat (z={oxygen_z:.2f})")
        
        if breaches:
            breached_patients.append((patient_id, breaches))
    
    # Print breached patients
    for patient_id, breaches in breached_patients:
        breach_str = ", ".join(breaches)
        print(f"{patient_id} | BREACH: {breach_str}")
    
    if not breached_patients:
        print("No vital sign breaches detected.")
    
    print()


# TASK 4: Triage Priority Report
def triage_report(patients, risk_dict):
    """Task 4: Generate final triage priority report"""
    print("====== TRIAGE PRIORITY REPORT ======")
    
    # Organize patients by category
    critical_patients = []
    moderate_patients = []
    stable_patients = []
    
    for patient in patients:
        patient_id = patient[0]
        age = patient[1]
        readmitted = patient[6]
        
        risk, category = risk_dict[patient_id]
        
        if category == "CRITICAL":
            critical_patients.append((patient_id, age, risk, readmitted))
        elif category == "MODERATE":
            moderate_patients.append((patient_id, age, risk, readmitted))
        else:
            stable_patients.append((patient_id, age, risk, readmitted))
    
    # Sort each category by risk score descending
    critical_patients.sort(key=lambda x: x[2], reverse=True)
    moderate_patients.sort(key=lambda x: x[2], reverse=True)
    stable_patients.sort(key=lambda x: x[2], reverse=True)
    
    # Print CRITICAL
    print(" CRITICAL ")
    for patient_id, age, risk, readmitted in critical_patients:
        readmitted_str = "YES" if readmitted == 1 else "NO"
        print(f"{patient_id} | Age: {age} | Risk: {risk:.3f} | Readmitted: {readmitted_str}")
    
    print()
    
    # Print MODERATE
    if moderate_patients:
        print(" MODERATE ")
        for patient_id, age, risk, readmitted in moderate_patients:
            readmitted_str = "YES" if readmitted == 1 else "NO"
            print(f"{patient_id} | Age: {age} | Risk: {risk:.3f} | Readmitted: {readmitted_str}")
        print()
    
    # Print STABLE
    if stable_patients:
        print(" STABLE ")
        for patient_id, age, risk, readmitted in stable_patients:
            readmitted_str = "YES" if readmitted == 1 else "NO"
            print(f"{patient_id} | Age: {age} | Risk: {risk:.3f} | Readmitted: {readmitted_str}")
        print()
    
    # Print summary
    print("=== CATEGORY SUMMARY ===")
    
    # Calculate readmission rates for each category
    if critical_patients:
        critical_readmitted = sum(1 for _, _, _, r in critical_patients if r == 1)
        critical_rate = (critical_readmitted / len(critical_patients)) * 100
        print(f"CRITICAL : {len(critical_patients)} patients | Readmission Rate: {critical_rate:.1f}%")
    
    if moderate_patients:
        moderate_readmitted = sum(1 for _, _, _, r in moderate_patients if r == 1)
        moderate_rate = (moderate_readmitted / len(moderate_patients)) * 100
        print(f"MODERATE : {len(moderate_patients)} patients | Readmission Rate: {moderate_rate:.1f}%")
    
    if stable_patients:
        stable_readmitted = sum(1 for _, _, _, r in stable_patients if r == 1)
        stable_rate = (stable_readmitted / len(stable_patients)) * 100
        print(f"STABLE : {len(stable_patients)} patients | Readmission Rate: {stable_rate:.1f}%")
    
    print()


# Main execution
if __name__ == "__main__":
    # Task 1: Profile patients
    profile_patients(patients)
    
    # Task 2: Risk scoring
    risk_dict = risk_score(patients)
    
    # Task 3: Breach detection
    breach_detector(patients)
    
    # Task 4: Triage report
    triage_report(patients, risk_dict)
