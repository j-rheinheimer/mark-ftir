program odair

implicit none
double precision, dimension(0:1866) :: a, b
double precision, dimension(0:208) :: c
character (9) :: filenm1
character (13) :: s
character (4) :: w
integer :: i, j

w = ".CSV"

! ESPECTRO NORMAL !

do j = 0,208

  write(filenm1,'(A,I3.3)') 'resin0',j
  s = filenm1 // w

  open(UNIT = j, FILE = s)

  do i = 1,1866
    read(j,*) a(i), b(i)
  enddo

  c(j) = b(1633)/b(1695)

  close(j)

enddo

open(UNIT = 1000, FILE = "25AA75DEG.txt")

do j = 0,208
  write(1000,*) c(j)
enddo

close(1000)

end program
