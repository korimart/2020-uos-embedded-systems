import glm

mat = glm.translate(glm.mat4(), glm.vec3(0, 1, 0))
translated = mat * glm.vec4(0, 0, 0, 1)
x, y, z = glm.vec3(translated)
print(x)