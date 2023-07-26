```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from problem_submission import Problem
from solution_submission import Solution

class SolutionEvaluator:
    def __init__(self):
        self.problem = Problem()
        self.solution = Solution()

    def evaluate_solution(self, problem_id, solution_id):
        problem_vector = self.problem.get_problem_vector(problem_id)
        solution_vector = self.solution.get_solution_vector(solution_id)

        similarity_score = self.calculate_similarity(problem_vector, solution_vector)

        return similarity_score

    def calculate_similarity(self, problem_vector, solution_vector):
        problem_vector = np.array(problem_vector).reshape(1, -1)
        solution_vector = np.array(solution_vector).reshape(1, -1)

        return cosine_similarity(problem_vector, solution_vector)[0][0]

    def rank_solutions(self, problem_id, solution_ids):
        scores = []
        for solution_id in solution_ids:
            score = self.evaluate_solution(problem_id, solution_id)
            scores.append((solution_id, score))

        scores.sort(key=lambda x: x[1], reverse=True)

        return scores
```