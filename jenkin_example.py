
import time

def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def main():
    print("🔧 Jenkins CI/CD Demo Running...")
    time.sleep(1)
    num = 5
    print(f"📦 Calculating factorial of {num}")
    result = factorial(num)
    print(f"✅ Factorial of {num} is {result}")
    print("🎉 Job completed successfully!")

if __name__ == "__main__":
    main()
