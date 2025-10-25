
from typing import List  # noqa: F403


# initialEnergy = 5
# initialExperience = 3
# energy = [1,4,3,2]
# experience = [2,6,3,1]


# initialEnergy = 2
# initialExperience = 4
# energy = [1]
# experience = [3]

initialEnergy = 5
initialExperience = 3
energy = [1,4]
experience = [2,5]

# initialEnergy = 1
# initialExperience = 1
# energy = [1,1,1,1]
# experience = [1,1,1,50]

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        training_hours_Experience = 0
        training_hours_Energy = 0

        if sum(energy) >= initialEnergy:
            training_hours_Energy = sum(energy) - initialEnergy + 1

        for exp in experience:
            if initialExperience > exp:
                initialExperience += exp
            else:
                
                diff = exp - initialExperience + 1
                training_hours_Experience += diff
                initialExperience += diff + exp  

        return training_hours_Experience + training_hours_Energy




s = Solution()
test = s.minNumberOfHours(initialEnergy,initialExperience,energy,experience)
print(test)







