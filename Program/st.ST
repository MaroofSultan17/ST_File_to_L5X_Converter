PROGRAM MainProgram
VAR
    iCount : INT;
    bOutput : BOOL;
END_VAR

// Initialize the variables
iCount := 0;
bOutput := FALSE;

// Main program loop
WHILE TRUE DO
    // Increment the counter
    iCount := iCount + 1;

    // Set the output if the counter is greater than 10
    IF iCount > 10 THEN
        bOutput := TRUE;
    END_IF;

    // Wait for 1 second
    DELAY 1s;
END_WHILE;

END_PROGRAM
