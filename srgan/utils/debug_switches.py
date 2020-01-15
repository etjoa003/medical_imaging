DEBUG_VERSION = 1

if DEBUG_VERSION:
	DEBUG_TRAINING_LOOP = 0
	DEBUG_TRAINING_DATA_LOADER_PRINT = 0
	DEBUG_TRAINING_SIZE_PER_RAW_BATCH = 100

	DEBUG_EVALUATION_SIZE_PER_RAW_TRAINING_BATCH = 100
	DEBUG_EVALUATION_SIZE_PER_RAW_TESTING_BATCH = 500
	DEBUG_EVALUATION_LOOP = 0

	DEBUG_NETWORK = 1
else:
	DEBUG_TRAINING_LOOP = 0
	DEBUG_TRAINING_DATA_LOADER_PRINT = 0
	DEBUG_TRAINING_SIZE_PER_RAW_BATCH = None


	DEBUG_EVALUATION_SIZE_PER_RAW_TRAINING_BATCH = None
	DEBUG_EVALUATION_SIZE_PER_RAW_TESTING_BATCH = None
	DEBUG_EVALUATION_LOOP = 0

	DEBUG_NETWORK = 0