"""Quiz: Most Frequent Word"""

def most_frequent(s):
  
    arr = s.split();
    arr.sort();
    m = 0;
    for each in arr:
        if(arr.count(each)>m):
            results = each;
            m = arr.count(each);
    
    return results


def test_run():
    """Test most_frequent() with some inputs."""
    print(most_frequent("cat bat mat cat bat cat")) # output: 'cat'
    print(most_frequent("betty bought a bit of butter but the butter was bitter")) # output: 'butter'


if __name__ == '__main__':
    test_run()
