''' This module provides a reusable byline for sumarizing company satisfaction statistics.'''

import math
import statistics
import random

company_name: str = "Williamson Cycling Analytics"
count_active_clients: int = 31
has_international_presence: bool = True
services_offered: list = ["Power Analysis", "Heart Rate Analysis", "Training Effectiveness"]
#random satisfaction scores created for all clients
satisfaction_scores = [random.uniform(1.0, 5.0) for _ in range(count_active_clients)]
average_client_satisfaction: float = round(statistics.mean(satisfaction_scores), 2)

#Create f-strings summarizig company information
active_clients_string: str = f"Active Clients: {count_active_clients}"
international_presence_string: str = f"International Presence: {has_international_presence}"
client_satisfaction_string: str = f"Average Client Satisfaction: {average_client_satisfaction}"
#Create string with out list brackets
sevices_str = ", ".join(services_offered) 
services_offered_string: str = f"Services Offered: {sevices_str}"

#Create satisfaction statistics and round all values to two decimal places
smallest= round(min(satisfaction_scores), 2)
largest= round(max(satisfaction_scores), 2)
total= round(sum(satisfaction_scores), 2)
count= len(satisfaction_scores)
mean= round(statistics.mean(satisfaction_scores), 2)
mode= round(statistics.mode(satisfaction_scores), 2)
median= round(statistics.median(satisfaction_scores), 2)
standard_deviation= round(statistics.stdev(satisfaction_scores), 2)

#Create string summarize all satisfaction statistics
stats_string: str = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Low: {smallest}
  High: {largest}
  Total: {total}
  Clients: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

#This byline generates a summary of company information and satisfaction statistics.
byline: str = f"""
{company_name}
{active_clients_string}
{international_presence_string}
{client_satisfaction_string}
{services_offered_string}
{stats_string}
"""

def main():
  ''' Display all output'''
  print(byline)

if __name__ == '__main__':
  main()