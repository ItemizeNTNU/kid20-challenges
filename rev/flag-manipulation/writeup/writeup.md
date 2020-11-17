# flag-manipulator:
## Description:
In this task an unlucky person has lost the flag in his file, and he has asked for your help to retrive it. Lucikly he has saved the last output the java code produced in the file output.txt. 

---
In the java file the flag has many manipulations done to it, the final flag is converted to byte array *b*. The [output.txt](output.txt) file consists of *b[0]*\*0+ *b[1]*\*1+*b[2]*\*0 and so on. In order to revert the changes we need to revert every function in the file and revert the order at which these manipulations are done. 
In addition to the manipulation functions the file reads bits from [bits.txt](bits.txt) and uses the native library file libstring.so which can be found in [flag-manipulator.zip](../files/flag-manipulator.zip). By inspecting the native library file, in an program like ghidra, we can find the function *getString*. The functions contains:
```
void Java_Manipulator_getString
               (long *param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5,undefined8 param_6)

{

  ...
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_98 = 0x68545f646c753043;
  local_90 = 0x54315f33625f3531;
  local_88 = 0x396c736737;
  
  ...

  (**(code **)(*param_1 + 0x538))
            (param_1,&local_98,&local_98,*(code **)(*param_1 + 0x538),param_5,param_6,param_2);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```
From this we can see that the function will return ``0x396c73673754315f33625f353168545f646c753043`` in reverted oder which results in ``C0uld_Th15_b3_1T7gsl9``. There are also other ways to retrive this string. 

 
The rest of the reversion can now happen in java and an example solution can be seen in [FlagManipulatorSolver.java](FlagManipulatorSolver.java).

The java class will return: ``KID20{j4va_exp3rt_0v3r_her3}``
