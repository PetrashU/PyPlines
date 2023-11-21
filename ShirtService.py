from Model import Shirt

class ShirtService:
    @staticmethod
    def GetAllShirts():
        return list(Shirt.select())

    @staticmethod
    def AddShirt(new_color, new_design):
        try:
            shirt = Shirt.create(color=new_color,design=new_design)
            return shirt
        except Exception as e:
            print("Error adding shirt: {}".format(e))
            return None

    @staticmethod
    def GetShirtById(shirt_id):
        return Shirt.get_or_none(id=shirt_id)

    @staticmethod
    def UpdateShirt(shirt_id, new_color, new_design):
        shirt = ShirtService.GetShirtById(shirt_id)
        if shirt:
            try:
                shirt.color = new_color
                shirt.design = new_design
                shirt.save()
                return shirt
            except Exception as e:
                print("Error updating shirt: {}".format(e))
                return None

    @staticmethod
    def DeleteShirt(shirt_id):
        shirt = ShirtService.GetShirtById(shirt_id)
        if shirt:
            try:
                shirt.delete_instance()
                return True
            except Exception as e:
                print("Error deleting shirt: {}".format(e))
                return False
        return False
