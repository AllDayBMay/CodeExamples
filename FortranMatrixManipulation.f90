!Below is the code to apply Fortran's dgtsv function to given input matrices
!In order to maintain the double-precision in the output matrices
!for the equation A*X=B (solving for X, where A is a tridiagonal matrix with n-by-n dimensions.
!I wrote this to solve a problem for my Scientific Computing course at ASU.

program p2_dgtsv
	!Declare variables
	use, intrinsic :: iso_fortran_env
	implicit none
	integer, parameter :: WP=REAL64
	character, parameter :: wp_type*6='REAL64'
	integer, parameter ::NRHS=1
	integer, parameter :: outunit=1000
	integer :: M,N
	integer :: info
	integer :: k
	real(WP) :: dx,x0=0,xN=1.,a
	real(WP),allocatable :: x(:),u(:),uex(:)
	real(WP),allocatable :: dl(:),d(:),du(:),b(:,:)
	character :: outfile*512
	
	!Collect further variables
	print *,'=============================='
	print *,'Input the discretization size (integer)
	read *, M
	print *, 'M was read as: ', M
	print *,'------------------------------'
	print *,'Input the parameter value, a (real WP ' // wp_type // '): '
	read *, a
	print *,'a was read as: ', a
	print *,'------------------------------'
	print *,'Name the output file: '
	read *, outfile
	print *,'Result will be written to file: ', outfile
	print *,'=============================='
	
	!Set matrices
	N = M + 1
	allocate(x(0:N),u(0:N),uex(0:N),dl(M),d(N),du(M),b(0:N,1))
	dx = (xN-x0)/float(N)
	x = [(x0+float(k)*dx, k=0,N)]
	
	b(1:M,1) = dx**2
	d1 = -(1. + a*dx)
	d = 2.
	du = -(1. - a*dx)
	
	!Apply Fortarn's dgtsv function to solve
	call dgtsv(M,NRHS,dl,d,du,b(1:M,1),M,info)
	
	!Print result
	if (info==0) then
		u(1:M) = b(1:M,1)
		uex = 1.+(exp(2.*a)-1.)*x-exp(2.*a*x)
		uex = uex / (2.*a*(exp(2.*a)-1.)
		b(1:M,1) = abs(u(1:M)-uex(1:M))/abs(uex(1:M))
		open(UNIT=outunit,file=outfile,status='replace')
		write(outunit,'(4(es28.16e3))') [ ([x(k),u(k),uex(k),b(k,1)],k=0,N)]
		close(outunit)
		print *, 'norm_2 rel_err: ', norm2(b)
	else
		print *, 'info = ',info
	end if
	
	deallocate(x,u,uex,dl,d,du,b)
	stop
end program p2_dgtsv

	
	
