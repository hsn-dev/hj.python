# print(dir())
# print(__file__.split('\\')[-1])

print("This will always be run!!!")

def main():
	print("Run Directly")
	print("First Module's Name: ", __name__)

if __name__ == '__main__':
	main()
else:
	print("Run From Import")