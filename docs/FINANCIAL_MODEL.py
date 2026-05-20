class FrosalindFinancialModel:
    """
    The "Forced Adoption" Calculator for Hospital CFOs.
    Calculates the profit gained from Bed-Day Recovery.
    """
    def __init__(self, hospital_beds=500, current_los=12, amr_rate=0.3):
        self.beds = hospital_beds
        self.current_los = current_los 
        self.amr_rate = amr_rate
        self.bed_day_cost = 15000 
        self.bed_day_revenue = 35000 

    def calculate_annual_impact(self, reduced_los=7):
        impacted_patients = (self.beds * 365 / self.current_los) * self.amr_rate
        days_saved = self.current_los - reduced_los
        total_days_recovered = impacted_patients * days_saved
        savings = total_days_recovered * self.bed_day_cost
        new_revenue = total_days_recovered * self.bed_day_revenue
        
        return {
            "Total_Bed_Days_Recovered": round(total_days_recovered),
            "Annual_Operational_Savings_INR": round(savings),
            "Annual_Opportunity_Revenue_INR": round(new_revenue),
            "Total_EBITDA_Impact_INR": round(savings + new_revenue)
        }

if __name__ == "__main__":
    model = FrosalindFinancialModel()
    impact = model.calculate_annual_impact()
    print("--- Frosalind: Hospital Financial Impact (500-Bed Facility) ---")
    for k, v in impact.items():
        print(f"{k}: {v:,} INR")
