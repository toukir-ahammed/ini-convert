How to Run ini_to_csv.py script:
1. put all .ini files in the following directory structure:
	-- raw
		-- tomcat
			-- tomcat
				-- AntiSingleton.ini
				-- BaseClassKnowsDerivedClass.ini
				.
				.
				.
				.
				-- TraditionBreaker.ini
2. Run the script using the following command:
	python ini_to_csv.py
3. Find the output csv file in the following directory:
	-- output
		-- tomcat
			-- tomcat.csv

Note: The script is tested in python 3.9
