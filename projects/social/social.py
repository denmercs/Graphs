import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def __repr__(self):
        f"{self.users}"

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship --> facebook
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            # This makes the two way connection between friends -> bi-directional
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()  # --> adjacency List

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments
        Creates that number of users and a randomly distributed friendships
        between those users.
        The number of users must be greater than the average number of friendships.
        import random
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users --> 1 though 10 to generate the users
        # Iterate: range from and including 0 to int(num_users)
        for n in range(0, int(num_users)):
            # create user up to num_users
            self.add_user(f"User: {n}")
        # print("Adding users" ,self.add_user(num_users) )

        # Create friendships --> total_friendships = avg_friendships * num_users
        possible_friendships = []
        # Create a list with all possible friendship combinations,
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # print('possible friendships:', possible_friendships, "\n")

        # shuffle the list,
        random.shuffle(possible_friendships)
        # print('poss-friend shuffle:', possible_friendships, "\n")

        # then grab the first N elements from the list.
        # Number of times to call add_friendship = avg_friendships * num_users/ 2
        for i in range(num_users * avg_friendships // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):  # BFS
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        measure distance between you and your friends
        """
        # print("User ID", user_id)

        visited = {}  # Note that this is a dictionary, not a set

        # Do a BFT to visit each user
        q = Queue()
        q.enqueue([user_id])
        # print("User ID", user_id)

        # While there is stuff in the queue
        while q.size() > 0:
            # Pop the first item in the path
            path = q.dequeue()
            # user = last item in the path
            user = path[-1]
            # print('User Id in path', user)

            # if not visited:
            if user not in visited:
                # add user to the visited dictionary as a list = path
                visited[user] = path
                # print("If in visited dictionary", visited)

                # If user_id is not in self. friendships dictionary
                if user_id not in self.friendships:
                    # print('user id not in friendships', self.friendships)
                    # return visited dictionary
                    return visited

                # for each friend in self.friendship(user id in path)
                for friend in self.friendships[user]:
                    # copy the values of path to path_copy variable
                    path_copy = path.copy()
                    # print('path copy', path_copy)

                    # append the friend to the path_copy
                    path_copy.append(friend)
                    # print("Appending friends to path_copy", path_copy)
                    # insert the path_copy to the Queue()
                    q.enqueue(path_copy)

        # Create an empty queue
        # add a PATH TO the starting vertex_id to the queue
        # create an empty dictionary to store visited users and social paths
        # while the queue is not empty...
            # dequeue, teh first path
            # Grab the last vertex from the path
            # check if it's been visited
            # if it has not been visited...
                # mark it as visited
                    # add it to the visited set, with the path as the key
                # then add all friends to the back of the queue
                    # copy the path
                    # add friend to the path

        return visited


if __name__ == '__main__':
    sg = SocialGraph()

    # Creates 10 users with an average of 2 friends each at the least. You and your friend
    sg.populate_graph(10, 2)
    print("--------------")
    print("friendships", sg.friendships)


    #    User_id  ________the friends user 1 is connected to generated randomly
    #      |    ___|___
    #      v   |      |
    # {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}} --these are also sets

    connections = sg.get_all_social_paths(1)
    print("--------------")
    print("connections", connections)

#                                  10 connects user 1 and user 2: 1 degree of seperation
#                                                      |
#                                                      v
#   {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
