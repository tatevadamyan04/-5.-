import numpy as np
from scipy import stats

# Данные
heights_mothers = np.array([172, 177, 158, 170, 178, 175, 164, 160, 169, 165])
heights_daughters = np.array([173, 175, 162, 174, 175, 168, 155, 170, 160])

# Рассчитаем среднее и стандартное отклонение для обеих выборок
mean_mothers = np.mean(heights_mothers)
std_mothers = np.std(heights_mothers, ddof=1)

mean_daughters = np.mean(heights_daughters)
std_daughters = np.std(heights_daughters, ddof=1)

# Выполним t-тест для двух независимых выборок
t_stat, p_value = stats.ttest_ind(heights_mothers, heights_daughters, equal_var=False)  # Assume unequal variances

# Результаты
print(f"Mean height of mothers: {mean_mothers:.2f}")
print(f"Standard deviation of mothers: {std_mothers:.2f}")
print(f"Mean height of daughters: {mean_daughters:.2f}")
print(f"Standard deviation of daughters: {std_daughters:.2f}")
print(f"Calculated t-statistic: {t_stat:.3f}")
print(f"p-value: {p_value:.3f}")

# Заключение:
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference in heights.")
else:
    print("Fail to reject the null hypothesis: No significant difference in heights.")

