class XYZ:
    def fi(self):
        try:
            a=int(input("Enter a number\n"))
        except Exception as e:
            print("Enter int only value of a")
        else:
            print(a)
        finally:
            print("Finally:Anyhow I will be printed")

x_obj_ref=XYZ
x_obj_ref.fi()
