<!DOCTYPE html>
<html>
<head>
    <title>Genre Table</title>
</head>
<body>
    <h1>${table} Table</h1>
    <table>
        <thead>
            <tr>
                
                % for field_name in field_names:
                <th>${field_name}</th>
                % endfor
            </tr>
        </thead>
        <tbody>
           
            % for row in data:
            <tr>
                % for item in row:
                <td>${item}</td>
                % endfor
            </tr>
            % endfor
        </tbody>
    </table>
</body>
</html>
