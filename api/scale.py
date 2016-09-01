def create_groups(group_name, scale_unit, scale):
    # Generate the prologue and the first scale unit
    groups =\
        '''{{
          "id": "/{0}",
          "groups": [
            {{
              "id": "/{0}/scale-unit-0",
              "apps": {1}
            }}
        '''.format(group_name, scale_unit)

    # Append the rest of scale units
    for x in range(1, scale):
        groups +=\
            '''
            ,{{
                "id": "/{0}/scale-unit-{2}",
                "dependencies": ["/{0}/scale-unit-{3}"],
                "apps": {1}
            }}
        '''.format(group_name, scale_unit, x, x - 1)

    # Close the epilogue
    groups +=\
        ''']
        }
        '''
    return groups
