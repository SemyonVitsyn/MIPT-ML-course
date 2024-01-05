import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """

    eigenvector = np.random.rand(data.shape[0])

    for i in range(num_steps):
      eigenvector = data @ eigenvector / np.linalg.norm(data @ eigenvector)

    return float((eigenvector.T @ data @ eigenvector) / (eigenvector.T @ eigenvector)), eigenvector