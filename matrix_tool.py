import numpy as np

def get_matrix(prompt):
    rows = int(input(f"Enter number of rows for {prompt}: "))
    cols = int(input(f"Enter number of columns for {prompt}: "))
    print(f"Enter elements of {prompt} row-wise:")
    elements = [float(input()) for _ in range(rows * cols)]
    return np.array(elements).reshape(rows, cols)

def main():
    while True:
        print("\nMatrix Operations Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("Choose an operation: ")

        if choice in ['1', '2', '3']:
            A = get_matrix("Matrix A")
            B = get_matrix("Matrix B")

            if choice == '1':
                result = A + B
                print("Result of Addition:\n", result)
            elif choice == '2':
                result = A - B
                print("Result of Subtraction:\n", result)
            elif choice == '3':
                result = np.dot(A, B)
                print("Result of Multiplication:\n", result)

        elif choice == '4':
            A = get_matrix("Matrix")
            print("Transpose:\n", A.T)

        elif choice == '5':
            A = get_matrix("Matrix (Square only)")
            if A.shape[0] == A.shape[1]:
                print("Determinant:", np.linalg.det(A))
            else:
                print("Matrix must be square!")

        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
