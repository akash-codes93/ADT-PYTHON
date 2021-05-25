"""
Suppose you have n doctors, each of which are free for a certain number of hours per day,
and  m  patients, each of whom needs to be seen for a certain number of hours. Write a
function that determines whether it's possible for all the patients to be scheduled so that
none of the doctors spends more time than they have available. Better yet, tell us which
people should see which doctors.
"""
from typing import List, Dict
from collections import defaultdict


# class Solution:
#
#     def get_available_doctors(self, doctors_schedule, patient):
#         doctors = []
#         for doctor in doctors_schedule:
#             if doctors_schedule[doctor] >= patient:
#                 doctors.append(doctor)
#
#         return doctors
#
#     def can_all_patients_be_seen(self, doctors_schedule, patients_schedule, schedule):
#
#         if not patients_schedule:
#             return True, schedule
#
#         if not doctors_schedule:
#             return False, {}
#
#         for patient in tuple(patients_schedule.keys()):
#
#             available_doctors = self.get_available_doctors(doctors_schedule, patients_schedule[patient])
#             if available_doctors:
#
#                 for doctor in available_doctors:
#                     org_patients_schedule = patients_schedule.copy()
#                     org_doctors_schedule = doctors_schedule.copy()
#                     org_schedule = schedule.copy()
#
#                     schedule[doctor].add(patient)
#                     doctors_schedule[doctor] -= patients_schedule[patient]
#                     patients_schedule.pop(patient)
#                     status, schedule = self.can_all_patients_be_seen(doctors_schedule, patients_schedule, schedule)
#                     if not status:
#                         patients_schedule = org_patients_schedule
#                         doctors_schedule = org_doctors_schedule
#                         schedule = org_schedule
#                     else:
#                         return status, schedule
#             else:
#                 return False, {}
#
#         return False, {}


class Solution2:

    def scheduling_result(self, doctors_schedule, patients_schedule, patients_list, schedule, patient_index):

        if patient_index >= len(patients_list):
            return True

        for doctor in doctors_schedule:
            if doctors_schedule[doctor] >= patients_schedule[patients_list[patient_index]]:
                doctors_schedule[doctor] -= patients_schedule[patients_list[patient_index]]
                if self.scheduling_result(doctors_schedule, patients_schedule, patients_list, schedule,
                                          patient_index + 1):
                    schedule[doctor].append(patients_list[patient_index])
                    return True
                else:
                    doctors_schedule[doctor] += patients_schedule[patients_list[patient_index]]

        return False

    def can_all_patients_be_seen(self, doctors_schedule, patients_schedule, schedule):

        patients_list = list(patients_schedule.keys())
        status = self.scheduling_result(doctors_schedule, patients_schedule, patients_list, schedule, 0)
        return status, schedule


schedule_d = {"kasdh1": 8, "ashd": 6, "asd": 3, "hdiv": 7}
schedule_p = {"asd": 2, "askdu": 3, "asgd": 6, "sdkf": 5, "uyfi": 1, "skjdhf": 4}

_schedule = Solution2().can_all_patients_be_seen({"d1": 9, "d2": 15},
                                                 {"p1": 3, "p3": 6, "p2": 9, "p4": 1}, defaultdict(list))
# _schedule = Solution2().can_all_patients_be_seen(schedule_d, schedule_p, defaultdict(list))

print(_schedule)

# all_combs(["d1", "d2"], ["p1", "p2", "p3"], 0, 0)
# caller({"d1": 8, "d2": 4}, {"p1": 6, "p2": 2, "p3": 2})
