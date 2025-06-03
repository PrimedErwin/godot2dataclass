from dataclasses import dataclass, field, asdict
import json

@dataclass
class Header:
    version_major: int
    version_minor: int
    version_patch: int
    version_status: str
    version_build: str
    version_full_name: str
    
@dataclass
class TypeSize:
    name: str
    size: int
    
@dataclass
class TypeBuildConfiguration:
    build_configuration: str
    sizes: list[TypeSize] = field(default_factory=list)
    
@dataclass
class BuiltinClassSizes:
    builtin_class_sizes: list[TypeBuildConfiguration] = field(default_factory=list)

@dataclass
class MemberOffset:
    member: str
    offset: int
    meta: str

@dataclass
class ClassMember:
    name: str
    members: list[MemberOffset] = field(default_factory=list)
    
@dataclass
class OffsetBuildConfiguration:
    build_configuration: str
    classes: list[ClassMember] = field(default_factory=list)

@dataclass
class BuiltinClassMemberOffsets:
    builtin_class_member_offsets: list[OffsetBuildConfiguration] = field(default_factory=list)

@dataclass
class GlobalConstants:
    global_constants: list = field(default_factory=list)

@dataclass
class EnumValues:
    name: str
    value: int

@dataclass
class GlobalEnum:
    name: str
    is_bitfield: bool
    values: list[EnumValues] = field(default_factory=list)

@dataclass
class GlobalEnums:
    global_enums: list[GlobalEnum] = field(default_factory=list)

@dataclass
class UtilityArguments:
    name: str
    type: str
    
@dataclass
class UtilityFunction:
    name: str
    return_type: str | None
    category: str
    is_vararg: bool
    hash: int
    arguments: list[UtilityArguments] | None = field(default_factory=list)
    
@dataclass
class UtilityFunctions:
    utility_functions: list[UtilityFunction] = field(default_factory=list)

@dataclass
class BuiltinClassOperator:
    name: str
    right_type: str
    return_type: bool
    
@dataclass
class BuiltinClassMember:
    name: str
    type: str
    
@dataclass
class BuiltinClassConstant:
    name: str
    type: str
    value: str
    
@dataclass
class BuiltinClassEnumValue:
    name: str
    value: int
    
@dataclass
class BuiltinClassEnum:
    name: str
    values: list[BuiltinClassEnumValue] | None= field(default_factory=list)
    
@dataclass
class BuiltinClassMehodArgument:
    name: str
    type: str
    default_value: str | None
    
@dataclass
class BuiltinClassMethod:
    name: str
    return_type: str | None
    is_vararg: bool
    is_const: bool
    is_static: bool
    hash: int
    arguments: list[BuiltinClassMehodArgument] | None = field(default_factory=list)
    
@dataclass
class BuiltinClassConstructorArgument:
    name: str
    type: str
    
@dataclass
class BuiltinClassConstructor:
    index: int
    arguments: list[BuiltinClassConstructorArgument] | None = field(default_factory=list)
    
@dataclass
class BuiltinClass:
    name: str
    indexing_return_type: str | None
    is_keyed: bool
    members: list[BuiltinClassMember] | None = field(default_factory=list)
    constants: list[BuiltinClassConstant] | None = field(default_factory=list)
    enums: list[BuiltinClassEnum] | None = field(default_factory=list)
    operators: list[BuiltinClassOperator] = field(default_factory=list)
    methods: list[BuiltinClassMethod] | None = field(default_factory=list)
    constructors: list[BuiltinClassConstructor] = field(default_factory=list)
    has_destructor: bool = field(default=False)
    
@dataclass
class BuiltinClasses:
    builtin_classes: list[BuiltinClass] = field(default_factory=list)

@dataclass
class ClassesEnumValue:
    name: str
    value: int

@dataclass
class ClassesEnum:
    name: str
    is_bitfield: bool
    values: list[ClassesEnumValue] | None = field(default_factory=list)
    
@dataclass
class ClassesConstant:
    name: str
    value: int
    
@dataclass
class ClassesMethodReturnValue:
    type: str
    meta: str | None
    
@dataclass
class ClassesMethodArgument:
    name: str
    type: str
    meta: str | None
    default_value: str | None
    
@dataclass
class ClassesMethod:
    name: str
    is_const: bool
    is_vararg: bool
    is_static: bool
    is_required: bool | None
    is_virtual: bool
    hash: int
    hash_compatibility: list[int] | None = field(default_factory=list)
    return_value: ClassesMethodReturnValue | None = field(default_factory=dict)
    arguments: list[ClassesMethodArgument] | None = field(default_factory=list)

@dataclass
class ClassesSignalArgument:
    name: str
    type: str
    
@dataclass
class ClassesSignal:
    name: str
    arguments: list[ClassesSignalArgument] | None = field(default_factory=list)

@dataclass
class ClassesProperty:
    type: str
    name: str
    setter: str | None
    getter: str | None
    index: str | None
    
@dataclass
class ClassesSingle:
    name: str
    is_refcounted: bool
    is_instantiable: bool
    inherits: str | None
    api_type: str
    constants: list[ClassesConstant] | None = field(default_factory=list)
    enums: list[ClassesEnum] | None = field(default_factory=list)
    methods: list[ClassesMethod] | None = field(default_factory=list)
    signals: list[ClassesSignal] | None = field(default_factory=list)
    properties: list[ClassesProperty] | None = field(default_factory=list)
    
@dataclass
class Classes:
    classes: list[ClassesSingle] = field(default_factory=list)

@dataclass
class Singleton:
    name: str
    type: str

@dataclass
class Singletons:
    singletons: list[Singleton] = field(default_factory=list)
    
@dataclass
class NativeStructure:
    name: str
    format: str
    
@dataclass
class NativeStructures:
    native_structures: list[NativeStructure] = field(default_factory=list)

@dataclass
class GodotInOne:
    header: Header
    builtin_class_sizes: list[TypeBuildConfiguration] = field(default_factory=list)
    builtin_class_member_offsets: list[OffsetBuildConfiguration] = field(default_factory=list)
    global_constants: list = field(default_factory=list)
    global_enums: list[GlobalEnum] = field(default_factory=list)
    utility_functions: list[UtilityFunction] = field(default_factory=list)
    builtin_classes: list[BuiltinClass] = field(default_factory=list)
    classes: list[ClassesSingle] = field(default_factory=list)
    singletons: list[Singleton] = field(default_factory=list)
    native_structures: list[NativeStructure] = field(default_factory=list)
    
def remove_none_values(obj):
    if isinstance(obj, dict):
        new_dict = {}
        for key, value in obj.items():
            if value is not None:
                new_value = remove_none_values(value)
                new_dict[key] = new_value
        return new_dict
    elif isinstance(obj, list):
        return [remove_none_values(item) for item in obj]
    else:
        return obj

def parse_builtin_class_sizes(json_data: dict) -> BuiltinClassSizes:
    build_configurations = []
    for config in json_data.get('builtin_class_sizes', []):
        sizes = [TypeSize(name=size_info['name'], size=size_info['size']) for size_info in config.get('sizes', [])]
        build_configuration = TypeBuildConfiguration(
            build_configuration=config.get('build_configuration'),
            sizes=sizes
        )
        build_configurations.append(build_configuration)

    return BuiltinClassSizes(builtin_class_sizes=build_configurations)

def parse_builtin_class_member_offsets(json_data: dict) -> BuiltinClassMemberOffsets:
    build_configurations = []
    for config in json_data.get('builtin_class_member_offsets', []):
        config_classes = []
        for classes in config.get('classes', []):
            members = [MemberOffset(member=member['member'],
                                    offset=member['offset'],
                                    meta=member['meta']) 
                       for member in classes.get('members', [])]
            config_classes.append(ClassMember(name=classes['name'],
                                              members=members))
        build_configurations.append(OffsetBuildConfiguration(build_configuration=config['build_configuration'],
                                                             classes=config_classes))
    return BuiltinClassMemberOffsets(builtin_class_member_offsets=build_configurations)
            
def parse_global_enums(json_data: dict) -> GlobalEnums:
    enums = []
    for enum in json_data.get('global_enums', []):
        values = [EnumValues(name=enum_value['name'],
                             value=enum_value['value'])
                  for enum_value in enum.get('values')]
        enums.append(GlobalEnum(name=enum['name'],
                                is_bitfield=enum['is_bitfield'],
                                values=values))
    return GlobalEnums(global_enums=enums)
            
def parse_utility_functions(json_data: dict) -> UtilityFunctions:
    utility_functions = []
    for func in json_data.get('utility_functions', []):
        arg_list = func.get('arguments', [])
        arguments = [UtilityArguments(name=arg['name'],
                                        type=arg['type'])
                    for arg in arg_list]
        if not arguments:
            arguments = None
        utility_functions.append(UtilityFunction(name=func['name'],
                                                 return_type=func.get('return_type'),
                                                 category=func['category'],
                                                 is_vararg=func['is_vararg'],
                                                 hash=func['hash'],
                                                 arguments=arguments))
    return UtilityFunctions(utility_functions=utility_functions)
   
def parse_builtin_classes(json_data: dict) -> BuiltinClasses:
    builtin_classes = []
    for builtin_class in json_data.get('builtin_classes', []):
        operators = [BuiltinClassOperator(name=operator['name'],
                                   right_type=operator.get('right_type'),
                                   return_type=operator['return_type'])
                  for operator in builtin_class.get('operators')]
        builtin_constructors = []
        for builtin_constructor in builtin_class.get('constructors', []):
            arg_list = builtin_constructor.get('arguments', [])
            arguments = [BuiltinClassConstructorArgument(name=arg['name'],
                                                         type=arg['type'])
                         for arg in arg_list]
            if not arguments:
                arguments = None
            constructor = BuiltinClassConstructor(index=builtin_constructor['index'],
                                                  arguments=arguments)
            builtin_constructors.append(constructor)
        member_list = builtin_class.get('members', [])
        members = [BuiltinClassMember(name=memb['name'],
                                      type=memb['type'])
                   for memb in member_list]
        if not members:
            members = None
        constant_list = builtin_class.get('constants', [])
        constants = [BuiltinClassConstant(name=const['name'],
                                          type=const['type'],
                                          value=const['value'])
                     for const in constant_list]
        if not constants:
            constants = None
        builtin_enums = []
        for builtin_enum in builtin_class.get('enums', []):
            enum_values = [BuiltinClassEnumValue(name=value['name'],
                                                value=value['value'])
                          for value in builtin_enum.get('values', [])]
            if not enum_values:
                enum_values = None
            enum = BuiltinClassEnum(name=builtin_enum['name'],
                                    values=enum_values)
            builtin_enums.append(enum)
        if not builtin_enums:
            builtin_enums = None
        builtin_methods = []
        for builtin_method in builtin_class.get('methods', []):
            method_arguments = [BuiltinClassMehodArgument(name=arg['name'],
                                                          type=arg['type'],
                                                          default_value=arg.get('default_value'))
                                for arg in builtin_method.get('arguments', [])]
            if not method_arguments:
                method_arguments = None
            method = BuiltinClassMethod(name=builtin_method['name'],
                                        return_type=builtin_method.get('return_type'),
                                        is_vararg=builtin_method['is_vararg'],
                                        is_const=builtin_method['is_const'],
                                        is_static=builtin_method['is_static'],
                                        hash=builtin_method['hash'],
                                        arguments=method_arguments)
            builtin_methods.append(method)
        if not builtin_methods:
            builtin_methods = None
        builtin_classes.append(BuiltinClass(name=builtin_class['name'],
                                            is_keyed=builtin_class['is_keyed'],
                                            indexing_return_type=builtin_class.get('indexing_return_type'),
                                            has_destructor=builtin_class['has_destructor'],
                                            members=members,
                                            constants=constants,
                                            enums=builtin_enums,
                                            methods=builtin_methods,
                                            constructors=builtin_constructors,
                                            operators=operators))
    return BuiltinClasses(builtin_classes=builtin_classes)
     
def parse_classes(json_data: dict) -> Classes:
    classes = []
    for classes_single in json_data.get('classes', []):
        classes_enums = []
        for classes_enum in classes_single.get('enums', []):
            value_list = classes_enum.get('values', [])
            values = [ClassesEnumValue(name=value['name'],
                                       value=value['value'])
                      for value in value_list]
            if not values:
                values = None
            enum = ClassesEnum(name=classes_enum['name'],
                               is_bitfield=classes_enum['is_bitfield'],
                               values=values)
            classes_enums.append(enum)
        if not classes_enums:
            classes_enums = None
        classes_constants = []
        constant_list = classes_single.get('constants', [])
        classes_constants = [ClassesConstant(name=constant['name'],
                                             value=constant['value'])
                             for constant in constant_list]
        if not classes_constants:
            classes_constants = None
        classes_methods = []
        for classes_method in classes_single.get('methods', []):
            return_values = classes_method.get('return_value', [])
            return_value = None
            if return_values:
                return_value = ClassesMethodReturnValue(type=return_values.get('type'),
                                                        meta=return_values.get('meta'))
            arg_list = classes_method.get('arguments', [])
            arguments = [ClassesMethodArgument(name=arg['name'],
                                              type=arg['type'],
                                              meta=arg.get('meta'),
                                              default_value=arg.get('default_value'))
                        for arg in arg_list]
            if not arguments:
                arguments = None
            method = ClassesMethod(name=classes_method['name'],
                                   is_const=classes_method['is_const'],
                                   is_vararg=classes_method['is_vararg'],
                                   is_static=classes_method['is_static'],
                                   is_virtual=classes_method['is_virtual'],
                                   is_required=classes_method.get('is_required'),
                                   hash=classes_method['hash'],
                                   hash_compatibility=classes_method.get('hash_compatibility'),
                                   arguments=arguments,
                                   return_value=return_value)
            classes_methods.append(method)
        if not classes_methods:
            classes_methods = None
        classes_signals = []
        for classes_signal in classes_single.get('signals', []):
            arg_list = classes_signal.get('arguments', [])
            arguments = [ClassesSignalArgument(name=arg['name'],
                                               type=arg['type'])
                         for arg in arg_list]
            if not arguments:
                arguments = None
            signal = ClassesSignal(name=classes_signal['name'],
                                   arguments=arguments)
            classes_signals.append(signal)
        if not classes_signals:
            classes_signals = None
        classes_properties = [ClassesProperty(type=arg['type'],
                                              name=arg['name'],
                                              setter=arg.get('setter'),
                                              getter=arg.get('getter'),
                                              index=arg.get('index'))
                              for arg in classes_single.get('properties', [])]
        if not classes_properties:
            classes_properties = None
        classes.append(ClassesSingle(name=classes_single['name'],
                                     is_refcounted=classes_single['is_refcounted'],
                                     is_instantiable=classes_single['is_instantiable'],
                                     inherits=classes_single.get('inherits'),
                                     api_type=classes_single['api_type'],
                                     enums=classes_enums,
                                     constants=classes_constants,
                                     methods=classes_methods,
                                     signals=classes_signals,
                                     properties=classes_properties))
    return Classes(classes=classes)
            
def parse_singletons(json_data: dict) -> Singletons:
    singletons = []
    for singleton in json_data.get('singletons', []):
        singletons.append(Singleton(name=singleton['name'],
                                    type=singleton['type']))
    return Singletons(singletons=singletons)

def parse_native_structures(json_data: dict) -> NativeStructures:
    native_structures = []
    for native_structure in json_data.get('native_structures', []):
        native_structures.append(NativeStructure(name=native_structure['name'],
                                                format=native_structure['format']))
    return NativeStructures(native_structures=native_structures)
   
   
if __name__ == '__main__':         
    file_path = 'extension_api.json'
    with open(file_path, 'r', encoding='utf-8') as fp:
        json_data = json.load(fp)
        
    result_header = Header(json_data['header'].get('version_major'),
                        json_data['header'].get('version_minor'),
                        json_data['header'].get('version_patch'),
                        json_data['header'].get('version_status'),
                        json_data['header'].get('version_build'),
                        json_data['header'].get('version_full_name'))
    result_builtin_class_sizes = parse_builtin_class_sizes(json_data)
    result_builtin_class_member_offsets = parse_builtin_class_member_offsets(json_data)
    result_global_constants = GlobalConstants()
    result_global_enums = parse_global_enums(json_data)
    result_utility_functions = parse_utility_functions(json_data)
    result_builtin_classes = parse_builtin_classes(json_data)
    result_classes = parse_classes(json_data)
    result_singletons = parse_singletons(json_data)
    result_native_structures = parse_native_structures(json_data)
    all_in_one = GodotInOne(header=result_header,
                            builtin_class_sizes=result_builtin_class_sizes.builtin_class_sizes,
                            builtin_class_member_offsets=result_builtin_class_member_offsets.builtin_class_member_offsets,
                            global_constants=result_global_constants.global_constants,
                            global_enums=result_global_enums.global_enums,
                            utility_functions=result_utility_functions.utility_functions,
                            builtin_classes=result_builtin_classes.builtin_classes,
                            classes=result_classes.classes,
                            singletons=result_singletons.singletons,
                            native_structures=result_native_structures.native_structures)
    cleared_none = remove_none_values(asdict(all_in_one))
    with open('output.json', 'w', encoding='utf-8') as fp:
        json.dump(cleared_none, fp, indent='\t')
        fp.write('\n')
    exit()