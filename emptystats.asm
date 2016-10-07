db ; pokedex id
db ; base hp
db ; base attack
db ; base defense
db ; base speed
db ; base special
db ; species type 1
db ; species type 2
db ; catch rate
db ; base exp yield
INCBIN "pic/bmon/.pic",0,1 ; , sprite dimensions
dw AbraPicFront
dw AbraPicBack
; attacks known at lvl 0
db 0
db 0
db 0
db 0
db 3 ; growth rate
; learnset
	tmlearn 1,5,6,8
	tmlearn 9,10
	tmlearn 17,18,19,20
	tmlearn 29,30,31,32
	tmlearn 33,34,35,40
	tmlearn 44,45,46
	tmlearn 49,50,55
db BANK(AbraPicFront)
