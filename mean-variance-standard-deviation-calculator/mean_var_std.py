import numpy as np

def calculate(list):
    try:
        input_array = np.array(list).reshape((3, 3))
    except ValueError:
        raise ValueError("List must contain nine numbers.")
    else:
        calculations = {
            'mean': [
                input_array.mean(0).tolist(),
                input_array.mean(1).tolist(),
                input_array.flatten().mean()
            ],
            'variance': [
                input_array.var(0).tolist(),
                input_array.var(1).tolist(),
                input_array.flatten().var()
            ],
            'standard deviation': [
                input_array.std(0).tolist(),
                input_array.std(1).tolist(),
                input_array.flatten().std()
            ],
            'max': [
                input_array.max(0).tolist(),
                input_array.max(1).tolist(),
                input_array.flatten().max()
            ],
            'min': [
                input_array.min(0).tolist(),
                input_array.min(1).tolist(),
                input_array.flatten().min()
            ],
            'sum': [
                input_array.sum(0).tolist(),
                input_array.sum(1).tolist(),
                input_array.flatten().sum()
            ]
        }
        return calculations

