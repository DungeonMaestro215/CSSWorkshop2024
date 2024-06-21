.section .data
message:
	.string "Hello, World!\n"


.section .text
.global _start

_start: 
	push   	%rbp
	mov    	%rsp,%r15
	pushq  	$0x0
	callq  	main
	mov    	$0x3c,%rax
	mov    	$0x0,%rdi
	syscall

main:
	push   	%rbp
	mov    	%rsp,%rbp

	mov 	$1, %rax
    mov 	$1, %rdi
    mov 	$message, %rsi
    mov 	$14, %rdx
    syscall
    
	mov    	%rbp,%rsp
	pop    	%rbp
	retq   	$0x8
	