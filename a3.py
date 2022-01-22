
import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        self.A=A
        self.alternative_A=self.A
 
    
    def translate(self, dx, dy):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        self.alternative_A=self.A
        super().translate(dx,dy)
        B=[]

        for i in range(len(self.A)):
          lst=[]
          for j in range(3):
            m=self.T_t[j][0]*self.A[i][0] + self.T_t[j][1]*self.A[i][1] + self.T_t[j][2]*self.A[i][2]
            lst.append(m)
          B.append(lst)
        B=np.array(B)
        self.A=B
        new1=np.array(B).transpose()
        new1=np.delete(new1,len(new1)-1,0)
        new1=np.around(new1,decimals=2)
        new_x_cord=new1[0]
        new_y_cord=new1[1]

        return new_x_cord,new_y_cord
    
    def scale(self, sx, sy):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        self.alternative_A=self.A
        Shape.scale(self,sx,sy)
        len1=len(self.A)
        temp1=np.array(self.A).transpose()
        x_cen= (sum(np.array(temp1)[0])) / len1
        y_cen= (sum(np.array(temp1)[1])) / len1
        l1=[]
        l2=[]
        l3=[]
        for i in range(len1):
            l1.append(x_cen)
            l2.append(y_cen)
            l3.append(1)

        xy_cen=np.array([l1,l2,l3])

        subt_mat=temp1-xy_cen
        mult_mat= np.dot(self.T_s,subt_mat)

        new_xy=mult_mat+xy_cen
        self.A=np.array(new_xy).transpose()                  #updating the value of A
        new_xy=np.delete(new_xy,len(new_xy)-1,0)
        new_xy=np.around(new_xy,decimals=2)
        new_x=new_xy[0]
        new_y=new_xy[1]

        return new_x, new_y

    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        Shape.rotate(self,deg)
        r1 = []
        r2 = []
        r3 = []
        for i in range(len(np.array(self.A).transpose()[0])):
            temp_r1 = r1.append(rx)
        for j in range(len(np.array(self.A).transpose()[1])):
            temp_r2 = r2.append(ry)
        for k in range(len(np.array(self.A).transpose()[0])):
            temp_r3 = r3.append(0)
        n_mat = np.array([r1, r2, r3])
        t_n_mat = np.array(n_mat.transpose())
        sub_matrix = (self.A - t_n_mat)
        n_mat2 = np.dot(sub_matrix, np.array(self.T_r).transpose())
        final_matrix = np.around((n_mat2 + t_n_mat), 2)
        t_final_matrix = np.array(final_matrix).transpose()
        self.x_new = t_final_matrix[0]
        self.y_new = t_final_matrix[1]
        self.old_matrix = self.A.copy()
        self.A = final_matrix
        return self.x_new, self.y_new

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        list1=[]
        list2=[]
        for j in range(len(self.alternative_A)):
            list1.append((self.alternative_A[j,0],self.alternative_A[j,1]))
        for i in range(len(self.A)):
            list2.append((self.A[i,0],self.A[i,1]))
        fig,ax=plt.subplots()
        poly_first=plt.Polygon(list1,linestyle='--',fill=False,linewidth=1.5)
        ax.add_patch(poly_first)
        poly_second=plt.Polygon(list2,fill=False,linewidth=1.5)
        ax.add_patch(poly_second)
        ax.set_aspect(1)
        t1=[]
        t2=[]

        for m in list1:                                             #t1 will give a list with only x coordinates of both updated and previous coordinate
            t1.append(abs(m[0]))
        for k in list2:
            t1.append(abs(k[0]))
        for n in list1:
            t2.append(abs(n[1]))
        for p in list2:
            t2.append(abs(p[1]))

        dim_pol_x=max(t1)
        dim_pol_y=max(t2)
        Shape.plot(self,dim_pol_x,dim_pol_y)




class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.x=x
        self.y=y
        self.radius=radius
        self.alternative_x=self.x
        self.alternative_y=self.y
        self.alternative_radius=self.radius



    
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        self.alternative_x=self.x
        self.alternative_y=self.y
        self.alternative_radius=self.radius

        Shape.translate(self,dx,dy)
        circle_cord=np.array([[self.x],[self.y],[1]])
        new_cord=np.dot(self.T_t,circle_cord)           #translating center

        self.x=float(new_cord[0])                              #updating the values of self.x and self.y
        self.y=float(new_cord[1])

        a1,b1,c1=np.around(self.x,decimals=2),np.round(self.y,decimals=2),float(np.round(self.radius,decimals=2))
        cord_tup=(a1,b1,c1)
        return cord_tup
 
        
    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        self.alternative_x=self.x
        self.alternative_y=self.y
        self.alternative_radius=self.radius
        self.radius=self.radius*sx
        cord_tup=(float(np.around(self.x,decimals=2)),float(np.around(self.y,decimals=2)),float(np.around(self.radius,decimals=2)))
        return cord_tup
 
    
    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        self.alternative_x=self.x
        self.alternative_y=self.y
        self.alternative_radius=self.radius
        self.A = [self.x, self.y, 1]
        Shape.rotate(self,deg)
        temp_matrix = np.array([rx, ry, 0])
        sub_matrix = np.subtract(self.A, temp_matrix)
        new_matrix = np.dot(sub_matrix, np.array(self.T_r).transpose())
        final_matrix = np.add(temp_matrix, new_matrix)
        self.x = float(np.around(final_matrix[0],decimals=2))
        self.y = float(np.around(final_matrix[1],decimals=2))
        cord_tup=(self.x,self.y,self.radius)

        return cord_tup

 
    
    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''

        circ1=plt.Circle((self.alternative_x,self.alternative_y),self.alternative_radius,fill=False,linestyle='--')
        fig=plt.figure()
        ax=fig.add_subplot(1,1,1)
        ax.add_patch(circ1)
        circ2=plt.Circle((self.x,self.y),self.radius,fill=False)
        ax.add_patch(circ2)
        ax.set_aspect(1)
        x_dim = max(self.radius + abs(self.x), self.alternative_radius + abs(self.alternative_x))
        y_dim = max(self.radius + abs(self.y), self.alternative_radius + abs(self.alternative_y))
        Shape.plot(self,x_dim,y_dim)


if __name__ == "__main__":

    verbos = int(input('Enter 1 for plotting after every transformation or press 0: '))
    if verbos==1 or verbos==0:
        test_cases = int(input('Enter the no. of test cases: '))
        ml = 1
        while ml <= test_cases:
            if verbos == 1:

                y = int(input('\nEnter 1 for circle or 0 for polygon: '))
                if y == 1:
                    z = list(map(float, input(
                        '\nEnter the co-ordinates of centre and the radius of circle(space separated): ').split()))
                    main_cord = (z[0], z[1], z[2])
                    sec_cord = main_cord
                    circle = Circle(z[0], z[1], z[2])

                    Q = int(input('\nEnter the number of queries: '))
                    print('\nR - Rotation')
                    print('T - Translation')
                    print('S - Scaling')
                    print('P - Plotting')
                    q1 = 0
                    while q1 < Q:
                        Queries = list(
                            map(str, input('\nEnter the query for the circle (space separated): ').split()))

                        if Queries[0] == 'T':
                            sec_cord = main_cord
                            if len(Queries) == 2:

                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                main_cord = circle.translate(float(Queries[1]), float(Queries[1]))
                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                circle.plot()
                            else:
                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                main_cord = circle.translate(float(Queries[1]), float(Queries[2]))
                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                circle.plot()

                        elif Queries[0] == 'S':
                            sec_cord = main_cord
                            for i in main_cord:
                                print(i, end=' ')
                            print()
                            main_cord = circle.scale(float(Queries[1]))
                            for i in main_cord:
                                print(i, end=' ')
                            print()
                            circle.plot()

                        elif Queries[0] == 'R':
                            sec_cord = main_cord
                            if len(Queries) == 2:

                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                main_cord = circle.rotate(float(Queries[1]))
                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                circle.plot()
                            else:
                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                main_cord = circle.rotate(float(Queries[1]), float(Queries[2]),
                                                       float(Queries[3]))
                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                circle.plot()

                        elif Queries[0] == 'P':
                            for i in sec_cord:
                                print(i, end=' ')
                            print()
                            for i in main_cord:
                                print(i, end=' ')
                            print()
                            circle.plot()

                        q1 = q1 + 1


                elif y == 0:
                    while True:

                        n = int(input('\nEnter the numer of sides of the polygon: '))
                        if n >= 3:
                            j = 0
                            k = []

                            while j < n:
                                r = list(map(float, input('\nEnter the co-ordinates of the polygon (space separated): ').split()))
                                r.append(1)
                                k.append(r)
                                j = j + 1

                            A = np.array(k)
                            cord_list = A.transpose()
                            cord_list = np.delete(cord_list, len(cord_list) - 1, 0)
                            new_list = cord_list
                            poly = Polygon(A)
                            Q = int(input('\nEnter the number of queries: '))
                            print('\nR - Rotation')
                            print('T - Translation')
                            print('S - Scaling')
                            print('P - Plotting')
                            q = 0
                            while q < Q:
                                Queries = list(
                                    map(str, input('\nEnter the query for the polygon (space separated): ').split()))

                                if Queries[0] == 'T':
                                    new_list = cord_list
                                    if len(Queries) == 2:
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()

                                        cord_list = poly.translate(float(Queries[1]), float(Queries[1]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        poly.plot()
                                    else:
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        cord_list = poly.translate(float(Queries[1]), float(Queries[2]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        poly.plot()

                                elif Queries[0] == 'S':
                                    new_list = cord_list
                                    if len(Queries) == 2:
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        cord_list = poly.scale(float(Queries[1]), float(Queries[1]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        poly.plot()
                                    else:
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        cord_list = poly.scale(float(Queries[1]), float(Queries[2]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        poly.plot()

                                elif Queries[0] == 'R':
                                    new_list = cord_list
                                    if len(Queries) == 2:

                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        cord_list = poly.rotate(float(Queries[1]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        poly.plot()
                                    else:
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        cord_list = poly.rotate(float(Queries[1]), float(Queries[2]),
                                                         float(Queries[3]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        poly.plot()
                                elif Queries[0] == 'P':
                                    for i in new_list:
                                        for j in i:
                                            print(j, end=' ')
                                    print()

                                    for i in cord_list:
                                        for j in i:
                                            print(j, end=' ')
                                    print()
                                    poly.plot()
                                q = q + 1



                        else:
                            print('\nInvalid input for number of side of polygon')
                        break


            elif verbos == 0:

                y = int(input('\nEnter 1 for circle or 0 for polygon: '))
                if y == 1:
                    z = list(map(float, input(
                        '\nEnter the co-ordinates of centre and the radius of circle(space separated): ').split()))
                    main_cord = (z[0], z[1], z[2])
                    circle = Circle(z[0], z[1], z[2])

                    Q = int(input('\nEnter the number of queries: '))
                    print('\nR - Rotation')
                    print('T - Translation')
                    print('S - Scaling')
                    print('P - Plotting')
                    q = 0
                    while q < Q:
                        Queries = list(
                            map(str, input('\nEnter the query for the circle (space separated): ').split()))

                        if Queries[0] == 'T':
                            sec_cord = main_cord
                            if len(Queries) == 2:

                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                main_cord = circle.translate(float(Queries[1]), float(Queries[1]))
                                for i in main_cord:
                                    print(i, end=' ')
                                print()

                            else:
                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                main_cord = circle.translate(float(Queries[1]), float(Queries[2]))
                                for i in main_cord:
                                    print(i, end=' ')
                                print()


                        elif Queries[0] == 'S':
                            sec_cord = main_cord
                            for i in main_cord:
                                print(i, end=' ')
                            print()
                            main_cord = circle.scale(float(Queries[1]))
                            for i in main_cord:
                                print(i, end=' ')
                            print()


                        elif Queries[0] == 'R':
                            sec_cord = main_cord
                            if len(Queries) == 2:

                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                main_cord = circle.rotate(float(Queries[1]))
                                for i in main_cord:
                                    print(i, end=' ')
                                print()

                            else:
                                for i in main_cord:
                                    print(i, end=' ')
                                print()
                                main_cord = circle.rotate(float(Queries[1]), float(Queries[2]),
                                                       float(Queries[3]))
                                for i in main_cord:
                                    print(i, end=' ')
                                print()

                        elif Queries[0] == 'P':
                            for i in sec_cord:
                                print(i, end=' ')
                            print()
                            for i in main_cord:
                                print(i, end=' ')
                            print()
                            circle.plot()

                        q = q + 1


                elif y == 0:
                    while True:

                        n = int(input('\nEnter the numer of sides of the polygon: '))
                        if n >= 3:
                            j = 0
                            k = []

                            while j < n:
                                r = list(map(float, input(
                                    '\nEnter the co-ordinates of the polygon (space separated): ').split()))
                                r.append(1)
                                k.append(r)
                                j = j + 1

                            A = np.array(k)
                            cord_list = A.transpose()
                            cord_list = np.delete(cord_list, len(cord_list) - 1, 0)
                            new_list = cord_list
                            poly = Polygon(A)
                            Q = int(input('\nEnter the number of queries: '))
                            print('\nR - Rotation')
                            print('T - Translation')
                            print('S - Scaling')
                            print('P - Plotting')
                            q = 0
                            while q < Q:
                                Queries = list(
                                    map(str, input('\nEnter the query for the polygon (space separated): ').split()))

                                if Queries[0] == 'T':
                                    new_list = cord_list
                                    if len(Queries) == 2:
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()

                                        cord_list = poly.translate(float(Queries[1]), float(Queries[1]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()

                                    else:
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        cord_list = poly.translate(float(Queries[1]), float(Queries[2]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()


                                elif Queries[0] == 'S':
                                    new_list = cord_list
                                    if len(Queries) == 2:
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        cord_list = poly.scale(float(Queries[1]), float(Queries[1]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()

                                    else:
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        cord_list = poly.scale(float(Queries[1]), float(Queries[2]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()


                                elif Queries[0] == 'R':
                                    new_list = cord_list
                                    if len(Queries) == 2:

                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        cord_list = poly.rotate(float(Queries[1]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()

                                    else:
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()
                                        cord_list = poly.rotate(float(Queries[1]), float(Queries[2]),
                                                         float(Queries[3]))
                                        for i in cord_list:
                                            for j in i:
                                                print(j, end=' ')
                                        print()

                                elif Queries[0] == 'P':
                                    for i in new_list:
                                        for j in i:
                                            print(j, end=' ')
                                    print()

                                    for i in cord_list:
                                        for j in i:
                                            print(j, end=' ')
                                    print()
                                    poly.plot()

                                q = q + 1

                            break

                        else:
                            print('\nInvalid input for number of side of polygon')

            ml += 1

    else:
        print('Wrong Input, please run the code again\n')



























